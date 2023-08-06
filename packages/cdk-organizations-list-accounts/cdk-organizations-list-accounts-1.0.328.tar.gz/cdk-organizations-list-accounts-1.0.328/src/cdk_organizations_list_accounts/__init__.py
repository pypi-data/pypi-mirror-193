'''
[![NPM version](https://badge.fury.io/js/cdk-organizations-list-accounts.svg)](https://badge.fury.io/js/cdk-organizations-list-accounts)
[![PyPI version](https://badge.fury.io/py/cdk-organizations-list-accounts.svg)](https://badge.fury.io/py/cdk-organizations-list-accounts)
![Release](https://github.com/hayao-k/cdk-organizations-list-accounts/workflows/release/badge.svg)

# cdk-organizations-list-accounts

Want to keep an up-to-date list of your AWS accounts?

cdk-organizations-list-accounts is an AWS CDK building library that outputs a list of AWS organization accounts in CSV format.

## Overview

Amazon EventBridge detects the account creation event and starts a Lambda function.
An accounts list, including the organization structure, will be output to S3 bucket in CSV format.

Output Example:

```csv
Id,Name,Email,Status,Joined Method,Joined Timestamp,OU Id,1st Level OU,2nd Level OU,3rd Level OU,4th Level OU,5th Level OU
000000000000,account-mgmt,account+mgmt@example.com,ACTIVE,INVITED,2022-01-31 07:19:57,r-xxxx
111111111111,account-0001,account+0001@example.com,ACTIVE,INVITED,2022-01-31 07:25:38,ou-xxxx-yyyyyyyy,Suspended
222222222222,account-0002,account+0002@example.com,ACTIVE,CREATED,2022-01-31 07:31:28,ou-xxxx-zzzzzzzz,Sample System,Additional,Workloads,Prod
333333333333,account-0003,account+0003@example.com,ACTIVE,CREATED,2022-01-31 08:15:49,ou-xxxx-zzzzzzzz,Sample System,Additional,Workloads,SDLC
444444444444,account-0004,account+0004@example.com,ACTIVE,CREATED,2022-01-31 09:18:50,ou-xxxx-zzzzzzzz,Sample System,Foundational,Security,Prod
555555555555,account-0005,account+0005@example.com,ACTIVE,CREATED,2022-01-31 10:21:30,ou-xxxx-zzzzzzzz,Sample System,Foundational,Infrastructure,Prod
666666666666,account-0006,account+0006@example.com,ACTIVE,CREATED,2022-01-31 11:21:05,ou-xxxx-zzzzzzzz,Sample System,Foundational,Infrastructure,SDLC
```

## Limitations at present

* Must deploy to AWS Organization's management account
* Events other than CreateAccount are not supported

## Getting Started

### TypeScript

Installation

```
$ yarn add cdk-organizations-list-accounts
```

Usage

```python
import * as cdk from 'aws-cdk-lib';
import { OrganizationsListAccounts } from 'cdk-organizations-list-accounts';

const App = new cdk.App();
const stack = new cdk.Stack(App, 'Stack', { env: { region: 'us-east-1' } });
new OrganizationsListAccounts(stack, 'Organizations-List-Accounts');
```

Deploy!

```
$ cdk deploy
```

### Python

Installation

```
$ pip install cdk-organizations-list-accounts
```

Usage

```py
import aws_cdk as cdk
from cdk_organizations_list_accounts import OrganizationsListAccounts

app = cdk.App()
stack = cdk.Stack(app, "Stack", env={"region": "us-east-1"})
OrganizationsListAccounts(stack, "Organizations-List-Accounts")
app.synth()
```

Deploy!

```
$ cdk deploy
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import constructs as _constructs_77d1e7e8


class OrganizationsListAccounts(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-organizations-list-accounts.OrganizationsListAccounts",
):
    '''
    :stability: experimental
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4983dd108701bdddab6f0abfd987b376605340ea14423689f9e296a2d05ba30)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])


__all__ = [
    "OrganizationsListAccounts",
]

publication.publish()

def _typecheckingstub__c4983dd108701bdddab6f0abfd987b376605340ea14423689f9e296a2d05ba30(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
