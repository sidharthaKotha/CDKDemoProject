#!/usr/bin/env python3

from aws_cdk import core

from cdk_project.cdk_project_stack import MyCrossAccountPipelineStack

app = core.App()
env_US = core.Environment(account=app.node.try_get_context('dev')['account'], 
                          region=app.node.try_get_context('dev')['region'])
env_EU = core.Environment(account=app.node.try_get_context('prod')['account'], 
                          region=app.node.try_get_context('prod')['region'])
MyCrossAccountPipelineStack(app, "myDevStack", env=env_US)
MyCrossAccountPipelineStack(app, "myProdStack", isProd=True, env=env_EU)
app.synth()
