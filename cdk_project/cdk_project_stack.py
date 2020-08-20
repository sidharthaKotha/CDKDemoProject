from aws_cdk import (
    aws_s3 as _s3,
    core
)

class MyCrossAccountPipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, isProd=False, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        if isProd:
            _s3.Bucket(
                self,
                "myProdArtifactBucket",
                bucket_name="mynewcdkprodbucket",
                versioned=True
            )
        else:
            _s3.Bucket(
                self,
                "myDevArtifactBucket"
            )
