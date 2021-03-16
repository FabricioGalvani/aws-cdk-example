#!/usr/bin/env python3

from aws_cdk import core as cdk
from s3_stack.s3 import S3Stack
# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from aws_cdk_exemplo.aws_cdk_exemplo_stack import AwsCdkExemploStack


app = cdk.App()
S3Stack(app, 'stack-cdk-bucket')
app.synth()
