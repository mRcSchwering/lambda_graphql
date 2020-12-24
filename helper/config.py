"""
Configure helper functions
"""

REPLACE = {
    "<account-id>": "my-aws-account",
    "<region>": "my-aws-region",
    "<stack-name>": "my-stack-name",
    "<api-deployment-id>": "api-deployment-id-from-sam-output",
}


def recursive_replace(obj):
    if isinstance(obj, dict):
        return {k: recursive_replace(d) for k, d in obj.items()}
    elif isinstance(obj, list):
        return [recursive_replace(d) for d in obj]
    elif isinstance(obj, str):
        s = obj
        for k, v in REPLACE.items():
            s = s.replace(k, v)
        return s
    return obj
