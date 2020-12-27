"""
Query resolvers
"""
from ariadne import QueryType  # type: ignore
from ariadne.types import GraphQLResolveInfo


query = QueryType()


@query.field("hello")
def resolve_hello(parent, info: GraphQLResolveInfo, **kwargs):
    return "Hello, %s!" % kwargs.get("name")


queries = (query,)
