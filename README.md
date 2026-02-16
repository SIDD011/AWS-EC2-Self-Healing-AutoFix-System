🚀 AWS EC2 Self-Healing AutoFix System
----

This project demonstrates a cloud-based self-healing infrastructure system built using AWS services.

When an EC2 instance’s CPU utilization exceeds a defined threshold, the system automatically:

- 🚨 Sends an SNS alert notification

- 🔁 Reboots the affected EC2 instance

- 📝 Logs the action in DynamoDB

- 💾 Creates an EBS snapshot for backup

This ensures automated incident response and improved infrastructure reliability.

---------------

🏗️ Architecture
----

Workflow:

1.CloudWatch monitors EC2 CPU utilization

2.If CPU > 80% for 2 consecutive minutes

3.CloudWatch Alarm triggers AWS Lambda

4.Lambda:

- Sends SNS alert

- Reboots EC2 instance

- Logs event to DynamoDB

- Creates EBS snapshot
- -------

🛠️ AWS Services Used
---

- EC2	Compute instance being monitored
- CloudWatch	Monitors CPU utilization and triggers alarm
- Lambda	Executes automated remediation logic
- SNS	Sends notification alerts
- DynamoDB	Stores remediation logs
- EBS Snapshot	Creates backup before reboot

------

⚙️ Lambda Function Logic
------

The Lambda function performs the following actions:

- Detects alarm trigger event

- Sends SNS alert

- Reboots EC2 instance

- Creates snapshot

- Logs action to DynamoDB with:

       - instanceId

       - timestamp

       - action description

-----

📂 DynamoDB Table Structure
------

Table Name: EC2-AutoFix-Logs

- Attribute	Type
- instanceId	String (Partition Key)
- timestamp	String (Sort Key)
- action	String

-----

📊 Monitoring
-------

- CPU Threshold: 80%

- Datapoints: 2 out of 2

- Evaluation period: 2 minutes

- Alarm state: Triggers Lambda automatically

- -----

🎯 Key Features
-------

- Fully automated EC2 recovery

- Event-driven architecture

- Cloud-native solution

- Real-time alerting

- Backup before remediation

- Logging for audit tracking
- -------

🔐 Security Considerations
------

- IAM roles used with least privilege principle

- No hardcoded credentials

- Resource-based policies applied where required

- -------

🧪 How to Test
------

1.Generate high CPU usage on EC2 instance:

     yes > /dev/null &


2.Wait for CloudWatch alarm to trigger

3.Verify:

     - EC2 reboot

    - SNS email alert

    - DynamoDB log entry

    - Snapshot creation
---------

📈 Learning Outcomes
---------

- AWS monitoring and alarms

- Event-driven automation

- Lambda + Boto3 integration

- Cloud incident response design

- Infrastructure self-healing concepts
