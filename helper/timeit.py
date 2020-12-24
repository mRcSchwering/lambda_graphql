"""
Time a request to API
"""
import time
import requests
from config import recursive_replace

URL = recursive_replace(
    "https://<api-deployment-id>.execute-api.<region>.amazonaws.com/dev/graphql/"
)

if __name__ == "__main__":
    body = {"data": "some data"}

    t0 = time.time()
    resp = requests.post(URL, json=body)
    td = time.time() - t0
    assert resp.ok, "Request response ok"
    print(f"Total: {td:.4f} ms")

