"""
Example test
"""
import json
from tests.conftest import event_fact
from graphql_post import lambda_handler  # type: ignore


def test_lambda_handler():
    event = event_fact('query { hello(name: "asd") }')
    resp = lambda_handler(event, "")
    assert resp["statusCode"] == 200

    data = json.loads(resp["body"])["data"]
    assert data["hello"] == "Hello, asd!"
