import boto3
import logging
from botocore.exceptions import ClientError, NoCredentialsError
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging to capture execution and debugging information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AWSAutomationController:
    """
    Manages AWS EC2 and S3 operations using Boto3, adhering to least-privilege principles.
    Includes robust error handling for AWS service limitations, IAM permissions, and Linux-level execution problems.
    """
    def __init__(self, region_name='us-east-1'):
        try:
            # Initialize Boto3 clients. This automatically looks for credentials stored in your system by `aws configure`
            self.ec2_client = boto3.client('ec2', region_name=region_name)
            self.s3_client = boto3.client('s3', region_name=region_name)
            logger.info("Successfully initialized Real AWS Boto3 clients.")
        except NoCredentialsError:
            logger.error("AWS credentials not found. Please run `aws configure` in your terminal.")
            raise

    def manage_ec2_instance(self, instance_id, action='start'):
        logger.info(f"Attempting to {action} EC2 instance: {instance_id}")
        try:
            if action == 'start':
                response = self.ec2_client.start_instances(InstanceIds=[instance_id])
                logger.info(f"Successfully initiated start for EC2 instance {instance_id}")
                return response
            elif action == 'stop':
                response = self.ec2_client.stop_instances(InstanceIds=[instance_id])
                logger.info(f"Successfully initiated stop for EC2 instance {instance_id}")
                return response
            else:
                raise ValueError("Invalid action. Must be 'start' or 'stop'.")
                
        except ClientError as e:
            error_code = e.response['Error']['Code']
            
            if error_code == 'UnauthorizedOperation':
                logger.error(f"IAM Permission Misconfiguration: The current IAM role lacks permissions to {action} this instance.")
            elif error_code in ['InvalidInstanceID.NotFound', 'IncorrectInstanceState', 'InvalidInstanceID.Malformed']:
                logger.error(f"AWS Service Error: Invalid instance ID or the instance is in a state that cannot be modified. Details: {e}")
            else:
                logger.error(f"An unexpected Boto3 ClientError occurred: {e}")
            
            return None

    def manage_s3_bucket(self, bucket_name, file_name, object_name=None):
        logger.info(f"Starting S3 upload operation to bucket: {bucket_name}")
        if object_name is None:
            object_name = file_name
            
        try:
            self.s3_client.upload_file(file_name, bucket_name, object_name)
            logger.info(f"Successfully uploaded {file_name} to s3://{bucket_name}/{object_name}")
            return True
            
        except boto3.exceptions.S3UploadFailedError as e:
            logger.error(f"S3 Upload Failed securely blocked: {e}")
            return None
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            
            if error_code == 'AccessDenied':
                logger.error(f"IAM Permission Boundary Hit: The IAM entity does not have 's3:PutObject' access to the bucket '{bucket_name}'.")
            elif error_code == 'NoSuchBucket':
                logger.error(f"AWS Service Error: The specified bucket '{bucket_name}' does not exist.")
            else:
                logger.error(f"An unexpected AWS S3 ClientError occurred: {e}")
                
            return None
            
        except FileNotFoundError:
            logger.error(f"Linux/OS Level Error: The file {file_name} was not found on the local filesystem.")
            return None


if __name__ == "__main__":
    logger.info("=== Starting Execution Against REAL AWS Infrastructure ===")
    
    automation_controller = AWSAutomationController()
    
    # ⚠️ Use environment variables for safety!
    REAL_INSTANCE_ID = os.getenv("AWS_INSTANCE_ID", "i-your-instance-id")
    REAL_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "aws-automation-project")
    
    logger.info("--- Executing Stop Instance ---")
    automation_controller.manage_ec2_instance(instance_id=REAL_INSTANCE_ID, action="stop")
    
    logger.info("--- Executing S3 Upload ---")
    automation_controller.manage_s3_bucket(bucket_name=REAL_BUCKET_NAME, file_name="README.md", object_name="uploaded_readme.md")
    
    logger.info("=== Real Execution Complete ===")
