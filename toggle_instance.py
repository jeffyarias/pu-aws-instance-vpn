import subprocess
import json
import os


# Function to get the state of the EC2 instance
def get_instance_state(instance_id):
    result = subprocess.run(['/usr/local/bin/aws', 'ec2', 'describe-instances', '--instance-ids', instance_id],
                            capture_output=True, text=True)
    if result.returncode == 0:
        output = json.loads(result.stdout)
        state = output['Reservations'][0]['Instances'][0]['State']['Name']
        return state
    else:
        print("Error describing instance:", result.stderr)
        return None


# Function to stop the EC2 instance
def stop_instance(instance_id):
    subprocess.run(['/usr/local/bin/aws', 'ec2', 'stop-instances', '--instance-ids', instance_id])


# Function to start the EC2 instance
def start_instance(instance_id):
    subprocess.run(['/usr/local/bin/aws', 'ec2', 'start-instances', '--instance-ids', instance_id])


# Main function
def main():
    instance_id = os.getenv('AWS_INSTANCE_ID')  # Replace with your EC2 instance ID
    state = get_instance_state(instance_id)
    if state == 'running':
        stop_instance(instance_id)
        print("Instance stopped.")
    elif state == 'stopped':
        start_instance(instance_id)
        print("Instance started.")
    else:
        print("Instance is in an unknown state.")


if __name__ == "__main__":
    main()
