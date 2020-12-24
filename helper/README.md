# Helper

Some helper functions that are annoying to always write again.

#### Deloy Policy Generator

See [setup.md](../setup.md).
Edit [config.py](./config.py) with `<account-id>`, `<region>`, `<stack-name>`.
Run below to get a policy JSON you can use for a deploy IAM user/role.

```
python helper/policy_gen.py
```

#### Test endpoint

Edit [config.py](./config.py) with `<api-deployment-id>` and `<region>`
.`<api-deployment-id>` is shown in the API URL of the SAM output or in AWS API Gateway console.
Edit [timeit.py](./timeit.py) with whatever payloads you want to test.
Then:

```
python helper/timeit.py
```
