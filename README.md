# Voice-Driven AWS Automation Manager

A full-stack, voice-controlled Amazon Web Services (AWS) infrastructure manager. This application allows you to operate EC2 instances and manage S3 backups securely using Natural Language Processing (Speech-to-Text), Python Boto3, and a Flask Backend.

![AWS Voice Manager](https://img.shields.io/badge/AWS-Boto3-FF9900?style=flat&logo=amazon-aws) 
![Frontend](https://img.shields.io/badge/Frontend-Vanilla_JS_&_SpeechRecognition-00d4ff) 
![Backend](https://img.shields.io/badge/Backend-Flask-000000?logo=flask)

## Project Architecture

This repository orchestrates critical infrastructure operations through robust Python scripting, replacing manual console operations with repeatable, secure automated processes:

### 1. Natural Language Processing Frontend
- A stunning glassmorphism browser interface utilizing the Web `SpeechRecognition` API.
- Converts spoken commands (e.g., *"boot up the server"*, *"shut down"*) into text payloads.
- Features manual-fallback S3 direct file uploading interfaces.

### 2. Flask API Backend (`app.py`)
- Acts as the deeply secure translation layer parsing the natural language intent.
- Applies fuzzy string-matching logic to route the spoken commands to the correct Boto3 AWS Python modules.

### 3. AWS Automation Layer (`aws_automation.py`)
- **EC2 Instance Management:** Automates the stopping and starting of specific compute instances.
- **S3 Storage Operations:** Securely manages data ingestion pipelines into S3 buckets.
- **Robust Error Handling:** Safely intercepts and catches AWS `ClientError` exceptions, `IncorrectInstanceState` rejections, and IAM Boundary `AccessDenied` errors.

---

## Security First: IAM Least-Privilege & Dotenv
We employ strict IAM policies attached to the automation execution role to prevent lateral movement or unintended destructive actions (see `iam_policies/ec2_s3_least_privilege.json`).

Furthermore, ALL specific AWS resource targets (Bucket Names and Instance IDs) are safely isolated into local `.env` variables and excluded from Version Control.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/voice-driven-aws-automation.git
   cd voice-driven-aws-automation
   ```

2. **Install dependencies:**
   Ensure you are using a Python virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials (CLI):**
   The Boto3 SDK relies on your machine's secure local AWS configuration.
   ```bash
   aws configure
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add your specific AWS resources:
   ```env
   # .env
   AWS_INSTANCE_ID="i-0xxxxxxxxx"
   AWS_BUCKET_NAME="your-s3-bucket-name"
   ```

## Usage

Start the Flask server locally:
```bash
python app.py
```

1. Open your browser to `http://localhost:5000`.
2. Allow Microphone access.
3. Click the Microphone Icon and confidently say:
   - *"Boot it up"*
   - *"Shut down the server"*
   - *"Upload backup to S3"*
4. Watch the UI immediately respond and trigger your live AWS Architecture!