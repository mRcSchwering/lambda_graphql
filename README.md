# Lambda GraphQL

AWS Lambda + API Gateway for deploying GraphQL endpoints using the [SAM framework](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).
This is basically the [SAM hello world app](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)
adapted for GraphQL endpoints.

- [SAM_README.md](./SAM_README.md) autogenerated README from SAM framework
- [template.yaml](./template.yaml) Lambda function and API gateway definitions for SAM framework
- [src/](./src/) code to be included in Lambda functions
- [helper/](./helper/) some tools to make development easier
- [tests/](./tests/) pytest suite

## tldr;

```
# local app
PYTHONPATH=./src uvicorn helper.app:app --reload

# tests
PYTHONPATH=./src pytest tests

# redeploy
sam build && sam deploy --parameter-overrides "ParameterKey=Stage,ParameterValue=dev"
```

## Setup

### Initial Stack Deploy

Initially deploy the **dev stage**
for a certain region, stack-name,
with admin cli user rights:

0. (Go through [template.yaml](./template.yaml) and find-replace `LambdaGraphql` if you want different names for those AWS resources)
1. `sam validate`
2. `sam build`
3. `sam deploy --parameter-overrides "ParameterKey=Stage,ParameterValue=dev" --guided`
   - Stack Name [sam-app]: **stack-name**
   - AWS Region [us-east-1]: **region**
   - Parameter Stage [dev]:
   - Confirm changes before deploy [y/N]: n
   - Allow SAM CLI IAM role creation [Y/n]: y
   - LambdaGraphQLFunction may not have authorization defined, Is this okay? [y/N]: y
   - Save arguments to configuration file [Y/n]: y
   - SAM configuration file [samconfig.toml]:
   - SAM configuration environment [default]:
4. test `curl https://<id>.execute-api.<region>.amazonaws.com/dev/graphql/` (SAM output shows URL)

Will create a (git-ignored) _samconfig.toml_. Afterwards `sam deploy` can be done without `--guided`.

### Deploy User

Make a IAM user or role for redeploying this stack.
Note: this user can do `sam build` and `sam deploy` but not `sam validate`.

1. Edit [helper/config.py](./helper/config.py) with `<account-id>`, `<region>`, `<stack-name>`
2. Run `python helper/policy_gen.py` to get policy JSON
3. Create new policy in AWS IAM with that policy JSON
4. Create new AWS IAM user or role with CLI capabilities and attach that policy
5. test by assuming that user/role (e.g. `aws configure`)
6. Try `sam build`, `sam deploy --parameter-overrides "ParameterKey=Stage,ParameterValue=dev"` with it

Always re-deploy with that IAM user/role: `sam build && sam deploy --parameter-overrides "ParameterKey=Stage,ParameterValue=dev"`.

## Tests

Run pytests in [tests/](./tests/). See [tests/conftest.py](./tests/conftest.py) for config.

```
PYTHONPATH=./src pytest tests
```

## Local App

There is a ASGI app in [helper/app.py](./helper/app.py) for easier GraphQL development locally.

```
PYTHONPATH=./src uvicorn helper.app:app --reload
```

## Delete

Go to AWS CloudFormation and delete the entire stack.
This should delete all resources (Lambda functions, API Gateways, roles, policies...).
