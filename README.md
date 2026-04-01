# AWS Automation Project

## Project Overview

**AWS Automation Project**
* Engineered Python-based workflows using the Boto3 SDK to automate the management of EC2 computing and S3 storage resources, implementing strict IAM least-privilege policies to ensure infrastructure security.
* Diagnosed and resolved complex execution failures, successfully addressing AWS service limitations, Linux OS-level errors, and IAM permission boundaries to guarantee highly reliable daily operations.

## Architecture & Workflows

This repository orchestrates critical infrastructure operations through robust Python scripting, replacing manual console operations with repeatable, secure automated processes:

### 1. EC2 Instance Management 
- Automates the stopping and starting of specific compute instances.
- Monitors and logs state changes.

### 2. S3 Storage Operations
- Securely manages data ingestion pipelines into S3 buckets.
- Handles Linux-level filesystem parsing and missing local file edge cases gracefully before upload attempts.

### 3. Error Handling & State Recovery
- **IAM Boundaries:** Deep error analysis catching `botocore.exceptions.ClientError` specifically for `AccessDenied` and `UnauthorizedOperation` to immediately diagnose misconfigurations.
- **Service Limits:** Accounts for invalid states (e.g., trying to start an instance that is already running or missing).
- **Linux Errors:** Manages local OS limitations (e.g. `FileNotFoundError` or permission denied during scheduled uploads).

## Security First: IAM Least-Privilege

We employ strict IAM policies attached to the automation execution role to prevent lateral movement or unintended destructive actions. Check the `iam_policies/ec2_s3_least_privilege.json` file to view the boundary restrictions.

- Access restricted by specific ARNs.
- Allows only specific Resource Tags (`Project` = `AWSAutomationWorkflow`).
- S3 access gated to dedicated pipeline buckets.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/aws-automation-project.git
   cd aws-automation-project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials:**
   The script relies on locally configured Boto3 credentials or server-assigned IAM roles (e.g., EC2 Instance Profile).
   ```bash
   aws configure
   ```

## Usage

You can test the execution workflow by running:
```bash
python aws_automation.py
```
*Note: Depending on your active AWS `region` and `credentials`, the script will gracefully catch missing EC2 instances and IAM boundary restrictions and print them as safely handled errors.*