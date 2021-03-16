from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3
)


class S3Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(scope, 
            id,
            bucket_name='meu-bucket-belisco-cdk'
        )
