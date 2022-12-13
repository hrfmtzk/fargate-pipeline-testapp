#!/usr/bin/env python3
import aws_cdk as cdk

from fargate_pipeline_testapp.fargate_pipeline_testapp_stack import (
    FargatePipelineTestappStack,
)

app = cdk.App()
FargatePipelineTestappStack(
    app,
    "FargatePipelineTestappStack",
)

app.synth()
