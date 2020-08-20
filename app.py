#!/usr/bin/env python3

from aws_cdk import core

from cdk_project.cdk_project_stack import CdkProjectStack


app = core.App()
CdkProjectStack(app, "cdk-project")

app.synth()
