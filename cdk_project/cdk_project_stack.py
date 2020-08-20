from aws_cdk import (
    aws_s3 as _s3,
    core
)

class CdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myCDKBucketLogicalID",
            bucket_name="mynewcdkbucket",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
