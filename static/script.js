let data = {
  name: "",
  subject: "",
  body: ""
};

function startDictation(field) {
  const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.start();

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    data[field] = transcript;
    document.getElementById(`${field}-display`).innerText = transcript;
    console.log(`${field}: ${transcript}`);
  };
}

function sendEmail() {
  fetch("/send_email", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(json => alert(json.message || json.error))
  .catch(err => alert("❌ Error: " + err));
}