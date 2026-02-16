import boto3
from datetime import datetime

# AWS Clients
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

# Configuration
INSTANCE_ID = "YOUR_INSTANCE_ID"
SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"
TABLE_NAME = "EC2-AutoFix-Logs"

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    timestamp = datetime.utcnow().isoformat()

    # Get attached volume ID
    response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
    volume_id = response['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']

    # Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=f"Auto snapshot before reboot - {timestamp}"
    )

    # Send SNS Alert
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="🚨 EC2 High CPU Alert",
        Message=f"""
High CPU detected!
Instance: {INSTANCE_ID}
Snapshot Created: {snapshot['SnapshotId']}
Time: {timestamp}
Action: Reboot initiated.
"""
    )

    # Log to DynamoDB
    table.put_item(
        Item={
            "instanceId": INSTANCE_ID,
            "timestamp": timestamp,
            "action": "Snapshot + Reboot triggered due to High CPU"
        }
    )

    # Reboot EC2
    ec2.reboot_instances(InstanceIds=[INSTANCE_ID])

    return {
        "statusCode": 200,
        "body": "Snapshot created, SNS sent, logged to DynamoDB, EC2 rebooted"
    }
