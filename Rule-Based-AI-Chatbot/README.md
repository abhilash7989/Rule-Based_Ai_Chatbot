# Rule-Based AI Chatbot 🤖

A professional, modular **rule-based chatbot** built with pure Python.
It responds to user messages using only deterministic `if-elif` logic and
dictionary lookups — **no machine learning**, **no external AI APIs**.

![Chatbot](assets/chatbot.png)

---

## 📖 Project Overview

This project demonstrates how a clean, well-structured chatbot can be built
without any AI/ML libraries. All conversational intelligence is expressed
through Python's standard library and a centralized response dictionary,
making the codebase easy to read, extend, and teach with.

---

## ✨ Features

- 👋 **Greetings** — `hi`, `hello`, `hey`, `good morning`, ...
- 🤖 **Self-introductions** — `who are you?`, `what can you do?`
- 📚 **Knowledge Q&A** — AI, Machine Learning, Python, Data Science, ChatGPT...
- 💬 **Small talk** — `how are you?`, `thank you`, `nice to meet you`
- 😂 **Jokes**, 💡 **fun facts**, 🌟 **quotes**, 💪 **motivations** (randomized)
- 🕒 **Date & time** via `datetime`
- 🧮 **Safe calculator** — `calculate 25 + 15`
- 🌦️ **Weather** — politely declines (offline bot)
- 📝 **Conversation history** auto-saved to `chat_history.txt`
- 🎨 **Colored terminal output** via `colorama`
- ⌨️ **Typing animation** for a natural feel
- ✅ **Input validation** + lowercase keyword matching
- 🧹 **PEP-8** style, modular functions, dictionary-driven responses

---

## 🗂️ Project Structure

```
Rule-Based-AI-Chatbot/
│
├── chatbot.py          # Main entry point and conversation loop
├── responses.py        # Centralized response data (dicts + lists)
├── requirements.txt    # Python dependencies
├── README.md           # You are here
└── assets/
    └── chatbot.png     # Project mascot
```

---

## 🛠️ Installation

1. **Clone or download** this repository.
2. (Recommended) create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

> The bot also runs without `colorama` — colors will simply be disabled.

---

## ▶️ How to Run

From the project root:

```bash
python .\Rule-Based-AI-Chatbot\chatbot.py
```

Type your messages at the `You:` prompt. Use `exit`, `quit`, or `bye` to leave.

---

## 💬 Example Conversation

```
========================================
        RULE BASED AI CHATBOT
========================================

Bot: Hello! I am your AI chatbot.
Bot: Type 'exit', 'quit', or 'bye' anytime to leave.

You: hello
Bot: Hello! Nice to meet you.

You: what is AI
Bot: Artificial Intelligence (AI) is the simulation of human intelligence
     by machines, enabling them to learn, reason, and make decisions.

You: calculate 25*4
Bot: 25*4 = 100

You: tell me a joke
Bot: Why do programmers prefer dark mode?
     Because light attracts bugs!

You: what time is it
Bot: The current time is 14:32:08.

You: bye
Bot: Goodbye! Have a wonderful day.
```

---

## 🚀 Future Improvements

- 🌐 Add a simple web UI (Flask / FastAPI + HTMX).
- 🗃️ Use regular expressions for more flexible intent matching.
- 🧠 Plug in an optional NLP layer (e.g. spaCy or rapidfuzz) for fuzzy keyword matching.
- 🌍 Multi-language responses.
- 🔌 Real weather data via OpenWeather API (opt-in).
- 🗣️ Voice input/output using `speech_recognition` and `pyttsx3`.
- 📊 Analytics on the most common user questions.

---

## 📝 License

Released under the MIT License — free to use, modify, and share.
