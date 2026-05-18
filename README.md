# Jarvis AI Assistant

A Python-based AI virtual assistant inspired by Jarvis. This assistant can recognize voice commands, open websites, play music, tell the time, and send WhatsApp messages using voice commands.

---

# Features

* Voice Recognition
* Wake Word Detection ("Jarvis")
* Text-to-Speech Response
* Open Websites using Voice Commands
* Play Music
* WhatsApp Message Automation
* Contact Recognition
* Time Feature
* Hands-free Interaction

---

# Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* pywhatkit
* webbrowser

---

# Project Structure

```bash
Jarvis-AI-Assistant/
│
├── main.py
├── musicLibrary.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/SivalankaLaxmi/Python-Repository.git
```

## 2. Go To Project Folder

```bash
cd Python-Repository
```

## 3. Create Virtual Environment

```bash
python -m venv env1
```

## 4. Activate Virtual Environment

### Windows

```bash
.\env1\Scripts\activate
```

---

# Install Required Libraries

```bash
pip install speechrecognition
pip install pyttsx3
pip install pywhatkit
pip install pyaudio
```

Or:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the project:

```bash
python main.py
```

Wake Jarvis using:

```bash
Jarvis
```

Example Commands:

```bash
Open Google
Open YouTube
Open LinkedIn
Play music
What is the time
Send message to mom
```

---

# WhatsApp Automation

Jarvis can send WhatsApp messages using voice commands.

Example:

```bash
You: Send message to mom
Jarvis: What should I send?
You: I will call you later
```

Requirements:

* WhatsApp Web login required
* Internet connection required
* Browser should remain open during automation

---

# Example Contact Dictionary

```python
contacts = {
    "mom": "+911234567890",
    "rahul": "+919876543210"
}
```

---

# Future Improvements

* ChatGPT Integration
* GUI Interface
* Weather Updates
* Email Automation
* AI Auto Replies
* Face Recognition
* Multi-language Support

---

# Screenshots

Add project screenshots here.

---

# Author

Sivalanka Laxmi

GitHub:
[https://github.com/SivalankaLaxmi](https://github.com/SivalankaLaxmi)
