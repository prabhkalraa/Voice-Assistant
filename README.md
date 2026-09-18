# 🎙️ Python Voice Assistant

A Python-based **JARVIS-style voice assistant** that allows users to perform everyday tasks using voice commands. The assistant combines speech recognition, text-to-speech, AI-powered responses, web automation, messaging, and AI image generation.

## ✨ Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech responses
* 🔎 Google Search
* 🎵 YouTube music playback
* 🕐 Time and date information
* 📝 Add, read, and display tasks
* 💻 Launch installed applications
* 📱 Send WhatsApp messages
* 🤖 AI-powered question answering
* 🎨 AI image generation from voice prompts

## 🛠️ Technologies & APIs

* **Python** — Core programming language
* **Google Speech Recognition** — Converts voice commands into text
* **pyttsx3** — Converts text responses into speech
* **Mistral AI API** — Processes AI-based user queries
* **Stability AI Stable Image Ultra API** — Generates images from text prompts
* **PyAutoGUI** — Application launching and keyboard automation
* **PyWhatKit** — WhatsApp and web automation
* **Plyer** — Desktop notifications
* **Web Browser** — Opens websites and generated images

## 🔌 APIs Used

### 1. Google Speech Recognition

The project uses the Google Speech Recognition service through the `SpeechRecognition` Python library to convert spoken commands into text.

```python
content = r.recognize_google(audio, language="en-in")
```

This allows the assistant to understand commands such as:

```text
"Play music"
"Tell time"
"Search Google Python"
"Ask AI what is machine learning"
```

### 2. Mistral AI API

AI-related commands are passed to a custom `mistral_ai.py` module, which communicates with the **Mistral AI API**.

```python
response = ai.send_request(request)
```

Example:

```text
Ask AI what is machine learning
```

The generated response is then spoken using `pyttsx3`.

### 3. Stability AI API

The image-generation feature uses the **Stability AI Stable Image Ultra API**.

API endpoint:

```text
https://api.stability.ai/v2beta/stable-image/generate/ultra
```

A voice command such as:

```text
Create image futuristic city
```

is converted into a text prompt and sent to Stability AI. The generated image is saved locally as:

```text
generated_image.webp
```

and opened automatically in the browser.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

**Do not put API keys directly inside your Python files or upload them to GitHub.**

Create a `.env` file:

```env
STABILITY_API_KEY=your_stability_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

Add `.env` to `.gitignore`:

```text
.env
__pycache__/
*.pyc
generated_image.webp
todo.txt
```

> The exact environment-variable name for Mistral should match the one used inside your `mistral_ai.py` file.

## ▶️ Run the Project

```bash
python main.py
```

After starting, the assistant waits for a voice command:

```text
Say something!
```

## 🎤 Example Commands

| Command                           | Function                          |
| --------------------------------- | --------------------------------- |
| `Hello`                           | Greets the user                   |
| `Play music`                      | Plays random YouTube music        |
| `Tell time`                       | Gives the current time            |
| `Tell date`                       | Gives the current date            |
| `Add task complete DSA`           | Adds a task                       |
| `Speak task`                      | Reads saved tasks                 |
| `Show task`                       | Shows tasks through notification  |
| `Open Chrome`                     | Launches an installed application |
| `Search Google Python`            | Searches Google                   |
| `Send WhatsApp`                   | Sends a WhatsApp message          |
| `Ask AI what is machine learning` | Gets an AI-generated response     |
| `Create image futuristic city`    | Generates an AI image             |
| `Bye`                             | Exits the assistant               |

## 🔄 How It Works

```text
Voice Input
     ↓
Google Speech Recognition
     ↓
Command Processing
     ↓
Identify Command
     ↓
┌───────────────────────────────┐
│ Google Search                 │
│ YouTube                       │
│ Task Management               │
│ Application Launcher         │
│ WhatsApp                      │
│ Mistral AI                    │
│ Stability AI Image Generation │
└───────────────────────────────┘
     ↓
Task Result
     ↓
pyttsx3 Text-to-Speech
```

## 📂 Project Structure

```text
Python-Voice-Assistant/
│
├── main.py
├── mistral_ai.py
├── image_form.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔐 Security

API keys are required for the AI and image-generation features.

**Never commit API keys to GitHub.**

Use environment variables or a `.env` file and keep `.env` inside `.gitignore`.

## 👨‍💻 Author

**Prabhmeet Singh**

B.Tech Computer Science & Engineering

GitHub: `github.com/prabhkalraa`
LinkedIn: `linkedin.com/in/prabhkalra`
