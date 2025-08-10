# voice-email-assistant
A Python-based voice-controlled assistant that allows users to send emails hands-free. It uses speech recognition to capture voice commands, converts them to text, and integrates with SMTP/Gmail API to compose and send messages securely. Designed for productivity, accessibility, and hands-free communication.

Features
-Send emails using only your voice.
-Recognizes both recipient details and message body from speech.
-Uses Flask for a lightweight web interface.
-Supports secure email sending via SMTP.
-Easy to configure and extend for custom commands.
-Can be integrated with AWS services for deployment.

Requirements
The project requires the following Python packages:
Flask
requests

Environment Variables (.env setup)
Create a file named .env in your project root and add the following:
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_generated_app_password
TOGETHER_API_KEY=your_together_ai_api_key

-EMAIL_ADDRESS → The sender’s email address.
-EMAIL_PASSWORD → App-specific password (e.g., Gmail App Password, not your normal login).
-TOGETHER_API_KEY → API key from Together AI.

How It Works
1.User speaks into the browser’s microphone.
2.Frontend JavaScript captures the voice, converts it to text, and sends it to Flask.
3.Flask backend passes the text to Together AI for processing.
4.Together AI LLM extracts details like recipient, subject, and message.
5.SMTP is used to send the email from your configured address.

Install them using:
pip install -r requirements.txt

Installation in terminal
1.Clone the Repository:
git clone https://github.com/prashanth-kaki/voice-email-assistant.git
cd voice-email-assistant

2.Create a Virtual Environment (Optional but Recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies:
pip install -r requirements.txt  #ignore it if you already installed

4.Configure Email Settings
-Open the configuration section in app.py
-Add your SMTP server details, email address, and password.
-For Gmail, enable "Less secure apps" or use an App Password.

Usage
1.Run the Application:
python app.py

2.Access in Browser
Open http://127.0.0.1:5000 in your web browser.

3.Send an Email
-Click the microphone button.
-Speak the recipient's email, subject, and message body.
-The assistant will process your input and send the email.

Project Structure
voice-email-assistant/
│
├── app.py               # Main application script
├── templates/           # HTML templates for Flask
├── static/              # CSS, JS, and assets
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Example Voice Command
"Send an email to John saying Meeting is postponed to 3 PM tomorrow."

The assistant will:
1.Recognize the command.
2.Extract recipient, subject, and body.
3.Send the email via SMTP.

Future Enhancements
-Integration with AWS SES for scalable email sending.
-Support for multiple email accounts.
-Advanced NLP for better context understanding.
-Voice feedback for confirmation.

License
This project is licensed under the MIT License - see the LICENSE file for details.

