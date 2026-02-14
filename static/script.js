let data = {
  name: "",
  subject: "",
  body: ""
};

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

function startDictation(field) {
  if (!SpeechRecognition) {
    alert("Speech Recognition is not supported in this browser.");
    return;
  }
  const recognition = new SpeechRecognition();
  recognition.lang = "en-US";

  try {
    recognition.start();
  } catch (e) {
    alert("Could not start mic. Please try again.");
    return;
  }

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    data[field] = transcript;
    const displayEl = document.getElementById(`${field}-display`);
    if (displayEl) {
      displayEl.innerText = transcript;
    }
    console.log(`${field}: ${transcript}`);
  };

  recognition.onerror = (event) => {
    if (event.error === 'network') {
      alert("Speech service unavailable. Please ensure you are using HTTPS and try again.");
    } else if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {
      alert("Microphone access denied. Please allow mic permissions.");
    } else if (event.error === 'no-speech') {
      alert("No speech detected. Please try again.");
    } else {
      alert("Mic error: " + event.error + ". Please try again.");
    }
  };
}

function sendEmail() {
  fetch("/send_email", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => {
    if (!res.ok) {
      return res.json().catch(() => ({ error: "Server error (" + res.status + ")" }));
    }
    return res.json();
  })
  .then(json => alert(json.message || json.error))
  .catch(err => alert("Failed to send email. Please check your connection."));
}