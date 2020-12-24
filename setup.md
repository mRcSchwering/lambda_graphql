# Setup

## Initial Stack Deploy

Initially deploy the **dev stage**
for a certain region, stack-name,
with admin cli user rights:

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

## Deploy User

Make a IAM user or role for redeploying this stack.
Note: this user can do `sam build` and `sam deploy` but not `sam validate`.

1. Edit [helper/config.py](./helper/config.py) with `<account-id>`, `<region>`, `<stack-name>`
2. Run `python helper/policy_gen.py` to get policy JSON
3. Create new policy in AWS IAM with that policy JSON
4. Create new AWS IAM user or role with CLI capabilities and attach that policy
5. test by assuming that user/role (e.g. `aws configure`)
6. Try `sam build`, `sam deploy --parameter-overrides "ParameterKey=Stage,ParameterValue=dev"` with it
