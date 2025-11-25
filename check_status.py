import boto3


def check_instance_status(region_name='us-east-1'):
    """
    Function to check and print the status of EC2 instances in the specified AWS region.
    """
    # Create an EC2 client
    ec2_client = boto3.client('ec2', region_name=region_name)

    try:
        # Retrieve all instance status checks
        response = ec2_client.describe_instance_status(IncludeAllInstances=True)

        # Parse the response
        for status in response['InstanceStatuses']:
            instance_id = status['InstanceId']
            state = status['InstanceState']['Name']  # e.g., running, stopped
            system_status = status['SystemStatus']['Status']  # e.g., ok, impaired
            instance_status = status['InstanceStatus']['Status']  # e.g., ok, impaired

            print(f"Instance ID: {instance_id}")
            print(f"State: {state}")
            print(f"System Status: {system_status}")
            print(f"Instance Status: {instance_status}")
            print("-" * 40)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    region = input("Enter the AWS region (default: us-east-1): ") or "us-east-1"
    check_instance_status(region)
