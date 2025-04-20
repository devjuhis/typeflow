# 🎙️ TypeFlow
<p align="center">
  <img src="https://github.com/devjuhis/typeflow/blob/main/assets/Typeflow_logo.png" width="300"/>
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://github.com/devjuhis/typeflow/stargazers"><img src="https://img.shields.io/github/stars/devjuhis/typeflow?style=social" alt="GitHub Stars"></a>
</p>

**Your AI-powered voice typing and writing assistant.**  
Built with Python, [Whisper](https://github.com/openai/whisper), [Groq AI](https://groq.com/), and `customtkinter`.

---

## ✨ Features

- 🎤 **Voice to Text** using OpenAI's Whisper
- 🤖 **Text Enhancement & Generation** with Groq AI
- 📋 **Live Logs** for both Whisper and AI outputs
- ⌨️ **Auto Input Insertion** – processed text is automatically typed into the focused input field
- 💡 **Lightweight GUI** built with `customtkinter`
- 🧪 Designed for writers, productivity nerds, accessibility use, and more!

---

## 📦 Installation

> Python 3.10+ recommended

1. **Clone the repo**

```bash
git clone https://github.com/devjuhis/typeflow.git
cd typeflow
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **create config.json**
```bash
api_key=your_groq_api_key
```

## 🧠 How It Works

- 🎙️ You speak → Whisper transcribes your voice to text.  
- 🤖 The text is sent to Groq AI for processing (can be rewritten, extended, cleaned, etc.).  
- 📋 Logs show what Whisper and AI are doing in real-time.  
- ⌨️ Processed text is injected into the focused input field.

---

## 🖼️ GUI Preview

<p align="center">
  <img src="https://github.com/devjuhis/typeflow/blob/main/assets/gui1.png" width="300"/>
  <img src="https://github.com/devjuhis/typeflow/blob/main/assets/gui2.png" width="300"/>
</p>

---

## 🛠 Tech Stack

- **Python** – core backend and logic  
- **customtkinter** – modern GUI for easy use  
- **Whisper (OpenAI)** – speech-to-text transcription  
- **Groq AI** – natural language processing & text transformation  
- **config.json** – secure API key handling  
- **keyboard** – for input field interaction

---

## 🧪 Use Cases

- 📝 Dictation & voice typing  
- ✍️ Writing assistant for bloggers, authors, and students  
- 💬 Accessibility tool for people with limited mobility  
- 🛠️ Voice-controlled input for creative or dev workflows

---

## 🗒️ Roadmap

- [ ] Voice command support (e.g., "new paragraph", "delete all")  
- [ ] Custom prompt templates for AI  
- [ ] Conversation log view in GUI  


