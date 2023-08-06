import json
from python_grains.profiles.exceptions import InvalidQuery, InvalidAudienceConfiguration

DEFAULT_REDIS_CLIENT = None
DEFAULT_DJANGO_AUDIENCE_MODEL = None
DEFAULT_DJANGO_CONNECTION_TUPLE = (None, None)
DEFAULT_DJANGO_MAX_FUNC = None
DEFAULT_AUDIENCE_TTL = 14 * 24 * 60 * 60
DEFAULT_AUDIENCE_DOMAINS = []
DEFAULT_DOMAIN = None
DEFAULT_AUDIENCE_ID_PREFIX = 'hic_au_'

ALLOWED_FIELD_TYPES = {
    'int': {
        'ops': ['$gt', '$lt', '$eq'],
        'validate': lambda x: isinstance(x, int)
    },
    'str': {
        'ops': ['$eq'],
        'validate': lambda x: isinstance(x, str)
    },
    'bool': {
        'ops': ['$eq'],
        'validate': lambda x: isinstance(x, bool)
    },
    'list': {
        'ops': ['$contains'],
        'validate': lambda x: isinstance(x, str)}
}

allowed_fields = {
    'lifetimeDvhNArticles': {'type': 'int',
                             'description': 'The total number of DvhN articles a visitor has viewed.'},
    'thirtyDaysDvhNArticles': {'type': 'int',
                               'description': 'The number of DvhN articles a visitor has viewed in the last thirty days.'},
    'lifetimeLCArticles': {'type': 'int',
                             'description': 'The total number of LC articles a visitor has viewed.'},}


class QueryAtom(object):

    def __init__(self,
                 var,
                 value,
                 operator):

        self.var = var
        self.value = value
        self.operator = operator
        self.validate()

    def validate(self):

        if self.var.startswith('$'):
            raise InvalidQuery(f'No operator allowed here: `{self.var}`')

        if not self.var in allowed_fields:
            raise InvalidQuery(f'Unknown field `{self.var}`')

        if not self.operator in ALLOWED_FIELD_TYPES[allowed_fields[self.var]['type']]['ops']:
            raise InvalidQuery(f'Invalid operator here: `{self.operator}` @ `{self.var}`')

        if not ALLOWED_FIELD_TYPES[allowed_fields[self.var]['type']]['validate'](self.value):
            raise InvalidQuery(f'Invalid value type for `{self.var}`, must be {allowed_fields[self.var]["type"]}')

    def run(self,
            value):

        if value is None:
            return False

        if self.operator == '$eq':
            return value == self.value

        elif self.operator == '$gt':
            return value > self.value

        elif self.operator == '$lt':
            return value < self.value

        elif self.operator == '$contains':
            return self.value in value

        else:
            raise InvalidQuery(f'Operator not implemented: {self.operator}')


class AudienceQuery(object):

    def __init__(self,
                 query,
                 op_c1=None,
                 name=None,
                 au_id=None,
                 raw_query=None):

        self.op_c1 = op_c1
        self.query = query
        self.name = name
        self.au_id = au_id
        self.raw_query = raw_query

    @classmethod
    def from_raw_data(cls, raw_data, op_c1=None, name=None):
        query_data = raw_data['query']
        au_id = raw_data['au_id']
        query = cls.parse(query_data)
        return cls(query=query, au_id=au_id, op_c1=op_c1, name=name, raw_query=query_data)

    @classmethod
    def parse_c1_operator_argument(cls,
                                   operator,
                                   argument):

        if operator in ('$or', '$and',):

            if not isinstance(argument, list):
                raise InvalidQuery(f'The `{operator}` operator expects a list')
            return AudienceQuery(argument, op_c1=operator)

        elif operator in ('$not',):

            if not isinstance(argument, dict):
                raise InvalidQuery(f'The `{operator}` operator expects a dictionary')

        else:
            raise InvalidQuery(f'Unknown operator {operator}')

        return AudienceQuery(argument, op_c1=operator)

    @classmethod
    def parse_query_atom(cls,
                         field_name,
                         value):

        if isinstance(value, (bool, int, float, str)):
            return QueryAtom(var=field_name, value=value, operator='$eq')

        elif isinstance(value, dict):
            if len(value) != 1:
                raise InvalidQuery(f'Invalid query for {field_name}')
            return QueryAtom(var=field_name, value=list(value.values())[0], operator=list(value.keys())[0])

        else:
            raise InvalidQuery(f'Invalid entry at `{field_name}`')

    @classmethod
    def parse(cls,
              raw_data):

        '''
        A recursive function that parses the audience query. It raises an InvalidQuery exception if
        the query is invalid. It returns an array with the parsed query when successful.
        '''

        parts = []

        if len(raw_data) == 0:
            raise InvalidQuery('Empty query is not allowed')

        if isinstance(raw_data, dict):

            for kw, v in raw_data.items():

                if kw.startswith('$'):

                    parts.append(cls.parse_c1_operator_argument(operator=kw, argument=v))

                else:

                    parts.append(cls.parse_query_atom(field_name=kw, value=v))

        elif isinstance(raw_data, list):

            for el in raw_data:
                parts.append(AudienceQuery(el))

        else:
            raise InvalidQuery('Query needs to be a list or a dictionary.')

        return parts

    def run(self, data):

        res = []

        for part in self.query:

            if isinstance(part, AudienceQuery):
                res.append(part.run(data))

            elif isinstance(part, QueryAtom):
                res.append(part.run(data.get(part.var)))

        if not self.op_c1 is None and self.op_c1 == '$or':
            return any(res)

        elif not self.op_c1 is None and self.op_c1 == '$not':
            return not all(res)

        elif not self.op_c1 is None and self.op_c1 == '$and':
            return all(res)

        else:
            return all(res)


class Audiences(object):

    django_audience_model = DEFAULT_DJANGO_AUDIENCE_MODEL
    django_connection_tuple = DEFAULT_DJANGO_CONNECTION_TUPLE
    django_max_func = DEFAULT_DJANGO_MAX_FUNC
    audience_ttl = DEFAULT_AUDIENCE_TTL
    redis_client = DEFAULT_REDIS_CLIENT
    domain = DEFAULT_DOMAIN
    audience_domains = DEFAULT_AUDIENCE_DOMAINS
    default_audience_id_prefix = DEFAULT_AUDIENCE_ID_PREFIX

    def __init__(self,
                 au_domain=None):

        self.au_domain = au_domain or '_global'
        self.queries = self.get_queries()

    def add(self,
            query,
            name='',
            description='',
            active=True,
            id_prefix=None,
            id_num=None):

        AudienceQuery.parse(query)

        id_prefix = id_prefix or self.default_audience_id_prefix

        if id_num is None:
            q = self.django_audience_model.objects.filter(id_prefix=id_prefix).aggregate(self.django_max_func('id_num'))
            id_num_max = q['id_num__max']

            if id_num_max is None:
                id_num_max = 0
            id_num = id_num_max + 1

        audience = self.django_audience_model(
            id_num=id_num,
            id_prefix=id_prefix,
            query=json.dumps(query),
            name=name,
            description=description,
            active=active,
            domain=self.au_domain)

        audience.save()
        self.build_cache()
        return audience

    def run(self,
            data):
        return [query.au_id for query in self.queries if query.run(data)]

    @classmethod
    def parse_query(cls, query):
        AudienceQuery.parse(raw_data=query)

    @classmethod
    def n_active(cls, au_domain):
        return cls.django_audience_model.objects.filter(domain=au_domain, active=True).count()

    @classmethod
    def list(cls, au_domain=None):

        if au_domain is None:
            audiences = [audience.repr_data for audience in cls.django_audience_model.objects.all()]
        else:
            audiences = [audience.repr_data for audience in cls.django_audience_model.objects.filter(domain=au_domain)]
            if not au_domain == '_global':
                audiences.extend(
                    [audience.repr_data for audience in cls.django_audience_model.objects.filter(domain='_global')])

        return audiences

    def get_queries(self,
                    force_db=False):

        if not force_db:
            audience_queries, raw_data = self.get_queries_from_cache()
        else:
            audience_queries, raw_data = None, None

        if audience_queries is None:

            audience_queries, raw_data = self.get_queries_from_db(au_domain=self.au_domain)

            if audience_queries is None:
                InvalidAudienceConfiguration('No valid audiences configuration found.')

            self.queries_to_cache(raw_data)

        return audience_queries

    def get_queries_from_cache(self):

        audiences = self.redis_client.get(self.cache_audiences_key)

        if not audiences is None:
            data = json.loads(audiences.decode())
            return [AudienceQuery.from_raw_data(raw_data=d) for d in data]
        else:
            return None

    @classmethod
    def get_queries_from_db(cls, au_domain):

        data = [a.short_data for a in cls.django_audience_model.objects.filter(active=True, domain=au_domain)]

        if not au_domain == '_global':
            data.extend([a.short_data for a in cls.django_audience_model.objects.filter(active=True, domain='_global')])

        audience_queries = [AudienceQuery.from_raw_data(raw_data=d) for d in data]

        return audience_queries, data

    def queries_to_cache(self,
                         audience_data):

        self._queries_to_cache(au_domain=self.au_domain, audience_data=audience_data)

    @classmethod
    def _queries_to_cache(cls,
                          au_domain,
                          audience_data):

        cls.redis_client.set(cls._cache_audiences_key(au_domain=au_domain), json.dumps(audience_data),
                             ex=cls.audience_ttl)

    def build_cache(self):

        self._build_cache(au_domain=self.au_domain)

    @classmethod
    def _build_cache(cls, au_domain=None):

        if au_domain is None or au_domain == '_global':
            au_domains = list(set(['_global', *cls.audience_domains]))
        else:
            au_domains = [au_domain]
        for d in au_domains:
            audience_queries, raw_data = cls.get_queries_from_db(au_domain=d)
            cls._queries_to_cache(au_domain=au_domain, audience_data=raw_data)

    @property
    def cache_audiences_key(self):

        return self._cache_audiences_key(au_domain=self.au_domain)

    @classmethod
    def _cache_audiences_key(cls, au_domain):

        return f'au:{cls.domain}:defs:{au_domain}'