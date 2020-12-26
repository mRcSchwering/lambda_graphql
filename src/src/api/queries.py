"""
Query resolvers
"""
from ariadne import QueryType  # type: ignore


query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    user_agent = "a user agent"
    return "Hello, %s!" % user_agent


queries = (query,)
