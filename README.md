# GPT-Based Smart Assistant

## Overview
This project is a **GPT-powered voice assistant** that allows users to interact using natural language. It leverages **speech recognition**, **OpenAI's GPT API**, and **text-to-speech conversion** to provide a seamless conversational experience.

## Features
- 🎙 **Voice Recognition**: Converts speech to text using `speech_recognition`.
- 🤖 **AI-Powered Responses**: Uses OpenAI's GPT model to process and respond to user queries.
- 🔊 **Text-to-Speech**: Converts AI-generated responses back into voice using `pyttsx3`.
- 🌐 **Web Browsing Commands**: Supports commands like opening Google, YouTube, etc.
- 🔒 **Secure API Handling**: Uses environment variables to protect API keys.

## Tech Stack
- **Python** 🐍
- **OpenAI GPT API** 🤖
- **SpeechRecognition** 🎙
- **Pyttsx3** 🔊
- **Webbrowser Module** 🌍
- **Dotenv** 🔐 (for secure API key storage)

## Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/lordpottercoding/GPT-Based-Smart-Assistant
cd gpt-smart-assistant
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key
Create a `.env` file in the project directory and add your **OpenAI API key**:
```
OPENAI_API_KEY=your-api-key-here
```

### 4️⃣ Run the Assistant
```sh
python main.py
```

## Usage
1. Run the script, and the assistant will greet you.
2. Speak your query when prompted.
3. The assistant will respond using AI-generated text and voice.
4. Say **'bye' or 'exit'** to close the assistant.

## Example Commands
- **"What is the capital of France?"**
- **"Tell me a joke."**
- **"Open YouTube."**
- **"What is AI?"**

## Future Enhancements 🚀
- Add integration with **Google Calendar** 📅
- Support for **home automation** devices 🏠
- Implement **multi-language support** 🌍

## License
This project is **MIT Licensed**. Feel free to use and modify it!

---
Made with ❤️ by LordPotterCoding