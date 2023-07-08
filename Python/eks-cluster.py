# Creating cluster using python
import boto3
from botocore.exceptions import ClientError

# Create an EKS client
EKS_CLUSTER_NAME = "eks-cluster"
EKS_REGION = "us-east-1"
EKS_ROLE_ARN = "0000000000000000000000000:role/eks-role"
EKS_VPC_ID = "0000000000000000000000000"
EKS_SUBNET_IDS = ["0000000000000000000000000", "0000000000000000000000000"]
EKS_NODE_TYPE = "t2.medium"
EKS_NODE_COUNT = 3
EKS_NODE_VOLUME_SIZE = 10
EKS_NODE_VOLUME_TYPE = "gp2"
EKS_NODE_VOLUME_IOPS = 0
EKS_NODE_VOLUME_ENCRYPTION = False
EKS_NODE_VOLUME_SNAPSHOT_ID = ""
EKS_NODE_VOLUME_TAGS = {}
EKS_NODE_VOLUME_MOUNT_POINT = "/var/lib/docker"
EKS_NODE_VOLUME_MOUNT_OPTIONS = ["defaults"]
EKS_NODE_VOLUME_FS_TYPE = "ext4"
EKS_NODE_VOLUME_FS_LABEL = ""
EKS_NODE_VOLUME_FS_OPTIONS = ["defaults"]
EKS_NODE_VOLUME_PROVISIONER = "aws"
EKS_NODE_VOLUME_IAM_ROLE = "AmazonEKSNodeVolumeController"


def create_eks_cluster():
    try:
        client = boto3.client("eks", region_name=EKS_REGION)
        response = client.create_cluster(
            name=EKS_CLUSTER_NAME,
            roleArn=EKS_ROLE_ARN,
            resourcesVpcConfig={
                "subnetIds": EKS_SUBNET_IDS,
                "endpointPublicAccess": False,
                "endpointPrivateAccess": False,
                "securityGroupIds": [],
            },
            version="1.14",
        )
        print(response)
    except ClientError as e:
        print(e)