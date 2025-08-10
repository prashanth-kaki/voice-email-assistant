from flask import Flask, render_template, request, jsonify
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

email_map = {
    "example-recipient-name": "forexample@gmail.com"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_email", methods=["POST"])
def send_email():
    data = request.json
    name = data.get("name", "").lower()
    subject = data.get("subject", "")
    body = data.get("body", "")

    if name not in email_map:
        return jsonify({"error": "Recipient not found"}), 400

    to_email = email_map[name]
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({"message": "✅ Email sent!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

