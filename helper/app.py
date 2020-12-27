"""
ASGI app for easier development

    PYTHONPATH=./src uvicorn helper.app:app --reload
"""
from ariadne.asgi import GraphQL  # type: ignore
from graphql_post import schema  # type: ignore

app = GraphQL(schema, debug=True)

