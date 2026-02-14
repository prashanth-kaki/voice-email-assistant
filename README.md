# 🎙️ Voice Email Assistant

A Python-based voice-controlled assistant that allows users to send emails hands-free. It uses speech recognition to capture voice commands, converts them to text, and integrates with SMTP/Gmail API to compose and send messages securely. Designed for productivity, accessibility, and hands-free communication.

## ✨ Features

- 🎤 Send emails using only your voice
- 🗣️ Recognizes recipient name, subject, and message body from speech
- 🌐 Uses Flask for a lightweight web interface
- 🔒 Supports secure email sending via SMTP
- ⚙️ Easy to configure and extend for custom commands
- ☁️ Can be integrated with AWS services for deployment
- 🔐 Secure configuration management (credentials not stored in repository)

## 📋 Requirements

The project requires the following Python packages:
- Flask
- requests

Install them using:
```bash
pip install -r requirements.txt
```

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/prashanth-kaki/voice-email-assistant.git
cd voice-email-assistant
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure User Settings (Important for Privacy)

#### Create your personal config file:
```bash
cp static/config.example.js static/config.js
```

#### Edit `static/config.js` with your details:
```javascript
window.CONFIG = {
  default_name: "Your Name",
  default_email: "your-email@example.com"
};
```

**Note:** The `config.js` file is gitignored and will NOT be committed to the repository, keeping your information private.

### 5. Update HTML to Load Config

Add this line in your `index.html` or `templates/index.html` in the `<head>` section, **before** the closing `</head>` tag:

```html
<script src="/static/config.js"></script>
<script src="/static/script.js"></script>
```

### 6. Configure Email Backend

#### Option A: Using Environment Variables (Recommended)

Create a file named `.env` in your project root and add:
```env
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_generated_app_password
TOGETHER_API_KEY=your_together_ai_api_key
```

- `EMAIL_ADDRESS` → The sender's email address
- `EMAIL_PASSWORD` → App-specific password (e.g., Gmail App Password)
- `TOGETHER_API_KEY` → API key from Together AI

#### Option B: Direct Configuration

Open `app.py` and configure:
```python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "your-email@gmail.com"
PASSWORD = "your-app-password"
```

**For Gmail Users:**
1. Enable 2-Factor Authentication
2. Generate an [App Password](https://myaccount.google.com/apppasswords)
3. Use that App Password (not your regular password)

## 🎯 How to Use

### Step 1: Start the Application
```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Step 2: Open in Browser
- Open your web browser
- Navigate to: `http://localhost:5000` or `http://127.0.0.1:5000`
- **Important:** Some browsers require HTTPS for microphone access

### Step 3: Grant Microphone Permission
- Click the microphone icon
- Your browser will ask for permission
- Click **"Allow"** to enable voice input

### Step 4: Send an Email

Click the 🎙️ microphone icon and speak through these steps:

1. **Recipient's Name**
   - Example: *"John Doe"*
   - Status updates to show name captured

2. **Email Subject**
   - Example: *"Meeting Tomorrow"*
   - Status updates to show subject captured

3. **Email Body/Message**
   - Example: *"Hi, let's meet at 3 PM to discuss the project"*
   - Status updates to show message captured

4. **Automatic Send**
   - Email is sent automatically after all inputs
   - You'll see a success or error message

## 💡 Usage Tips

### ✅ Best Practices
- Speak clearly and at a normal pace
- Wait for the status to update before speaking again
- Use HTTPS connection for better speech recognition
- Ensure you're in a quiet environment
- Test microphone before starting

### ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Microphone not working | Check browser permissions in Settings |
| "Speech service unavailable" | Ensure you're using HTTPS or localhost |
| "No speech detected" | Speak louder or check microphone settings |
| Email not sending | Verify SMTP configuration in `app.py` |
| Config not loading | Ensure `config.js` is created and HTML is updated |

## 🔧 How It Works

1. User speaks into the browser's microphone
2. Frontend JavaScript captures the voice using Web Speech API
3. Speech is converted to text in real-time
4. Data is sent to Flask backend via POST request
5. Backend processes the data and sends email via SMTP
6. User receives confirmation message

## 📁 Project Structure

```
voice-email-assistant/
│
├── app.py                    # Main Flask application
├── templates/                # HTML templates
│   └── index.html           # Main UI template
├── static/                   # Static assets
│   ├── script.js            # Voice recognition logic
│   ├── config.example.js    # Config template (committed)
│   └── config.js            # Personal config (gitignored)
├── requirements.txt          # Python dependencies
├── .gitignore               # Prevents sensitive files from being committed
├── README.md                # This file
└── LICENSE                  # MIT License

```

## 🎬 Example Usage

**Voice Command:**
> "Send an email to John saying Meeting is postponed to 3 PM tomorrow."

**What Happens:**
1. ✅ Recognizes the command
2. ✅ Extracts recipient, subject, and body
3. ✅ Sends the email via SMTP
4. ✅ Displays success message

## 🌐 Browser Compatibility

Works best with:
- ✅ Google Chrome (Recommended)
- ✅ Microsoft Edge
- ✅ Safari (macOS/iOS)
- ⚠️ Firefox (Limited Web Speech API support)

## 🔒 Security & Privacy

- ✅ Personal configuration files are gitignored
- ✅ Credentials never stored in repository
- ✅ Uses secure SMTP connections
- ✅ App Passwords instead of account passwords
- ✅ Config template provided for easy setup

## 🚀 Future Enhancements

- Integration with AWS SES for scalable email sending
- Support for multiple email accounts
- Advanced NLP for better context understanding
- Voice feedback for confirmation
- Email templates and scheduling
- Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Made with ❤️ for hands-free email communication