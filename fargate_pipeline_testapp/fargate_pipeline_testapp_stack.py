from aws_cdk import (
    Stack,
    aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpactions,
    aws_ecr as ecr,
)
from constructs import Construct


class FargatePipelineTestappStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        target_branch_name: str = "main",
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = codepipeline.Pipeline(
            self,
            "Pipeline",
        )
        source_artifact = codepipeline.Artifact("source_artifact")
        repository = ecr.Repository(
            self,
            "Repository",
        )

        pipeline.add_stage(
            stage_name="Source",
            actions=[
                cpactions.CodeCommitSourceAction(
                    output=source_artifact,
                    repository=codecommit.Repository(
                        self,
                        "Repository",
                        repository_name="testapp-repository",
                    ),
                    branch=target_branch_name,
                    trigger=cpactions.CodeCommitTrigger.EVENTS,
                    action_name="Source",
                ),
            ],
        )

        build_project = codebuild.PipelineProject(
            self,
            "BuildProject",
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.STANDARD_6_0,
            ),
        )
        repository.grant_pull_push(build_project)
        pipeline.add_stage(
            stage_name="Build",
            actions=[
                cpactions.CodeBuildAction(
                    input=source_artifact,
                    project=build_project,
                ),
            ],
        )

        # pipeline.add_stage(
        #     stage_name="Deploy",
        #     actions=[
        #         cpactions.EcsDeployAction(),
        #     ],
        # )
