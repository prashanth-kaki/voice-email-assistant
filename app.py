from flask import Flask, render_template, request, jsonify
from aws_automation import AWSAutomationController
import logging
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load secret environment variables
load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure your AWS Resources securely from the .env file
REAL_INSTANCE_ID = os.getenv("AWS_INSTANCE_ID", "")
REAL_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/aws_command", methods=["POST"])
def aws_command():
    data = request.get_json(silent=True)
    if not data or "command" not in data:
        return jsonify({"error": "No voice command provided."}), 400
        
    command_text = data.get("command", "").lower().strip()
    logger.info(f"Received Voice Command: '{command_text}'")
    
    try:
        # Initialize the AWS Boto3 Controller automatically using local aws configure credentials
        aws_controller = AWSAutomationController()
    except Exception as e:
        return jsonify({"error": f"Failed to connect to AWS: {str(e)}"}), 500

    # Command Router Logic - Fuzzy Matching
    if any(word in command_text for word in ["start", "boot", "run", "launch", "turn on"]):
        return _handle_ec2(aws_controller, action="start")

    elif any(word in command_text for word in ["stop", "shut down", "shutdown", "halt", "kill", "turn off"]):
        return _handle_ec2(aws_controller, action="stop")

    elif any(word in command_text for word in ["upload", "backup", "s3", "save"]):
        return _handle_s3(aws_controller)
        
    else:
        return jsonify({"error": f"Command '{command_text}' wasn't recognized. Try 'Start the server' or 'Upload file'."}), 400

def _handle_ec2(aws_controller, action):
    # Triggers the AWS automation script gracefully
    response = aws_controller.manage_ec2_instance(instance_id=REAL_INSTANCE_ID, action=action)
    if response:
        return jsonify({"message": f"Successfully issued command to {action} EC2 instance: {REAL_INSTANCE_ID}"})
    else:
        return jsonify({"error": f"Failed to {action} EC2 instance. Check IAM Permissions and valid Instance ID."}), 500

def _handle_s3(aws_controller):
    # Simulates uploading the README (or any local file) as a backup task
    local_file = "README.md"
    upload_target = "voice_command_backup.md"
    
    response = aws_controller.manage_s3_bucket(bucket_name=REAL_BUCKET_NAME, file_name=local_file, object_name=upload_target)
    if response is not None:
        return jsonify({"message": f"Successfully backed up {local_file} to s3://{REAL_BUCKET_NAME}/{upload_target}!"})
    else:
        return jsonify({"error": "Failed S3 Upload. Check IAM boundary policies and ensure bucket exists."}), 500

@app.route("/api/upload_s3", methods=["POST"])
def upload_s3():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    filename = secure_filename(file.filename)
    
    # Save the file temporarily to use the boto3 upload_file method
    temp_path = os.path.join(app.root_path, filename)
    file.save(temp_path)
    
    try:
        aws_controller = AWSAutomationController()
        response = aws_controller.manage_s3_bucket(bucket_name=REAL_BUCKET_NAME, file_name=temp_path, object_name=filename)
        
        # Cleanup temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
        if response is not None:
            return jsonify({"message": f"Successfully uploaded {filename} to S3 bucket: {REAL_BUCKET_NAME}!"})
        else:
            return jsonify({"error": "Failed S3 Upload. Check IAM boundary policies."}), 500
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({"error": f"Failed to connect to AWS: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
