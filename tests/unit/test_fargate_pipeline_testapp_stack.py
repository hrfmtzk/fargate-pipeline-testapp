import aws_cdk as core
import aws_cdk.assertions as assertions

from fargate_pipeline_testapp.fargate_pipeline_testapp_stack import FargatePipelineTestappStack

# example tests. To run these tests, uncomment this file along with the example
# resource in fargate_pipeline_testapp/fargate_pipeline_testapp_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FargatePipelineTestappStack(app, "fargate-pipeline-testapp")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
