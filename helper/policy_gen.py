"""
Generate policy for a IAM user/role that can deploy the stack
"""
import json
from config import recursive_replace


def load_policy(file: str) -> dict:
    with open(file, "r") as fh:
        return json.load(fh)


if __name__ == "__main__":
    policy = load_policy("helper/deploy-policy.json")
    print(json.dumps(recursive_replace(policy), indent=4, sort_keys=True))
