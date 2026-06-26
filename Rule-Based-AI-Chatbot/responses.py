"""
responses.py
------------
Centralized response data for the Rule-Based AI Chatbot.

Using dictionaries and lists here keeps `chatbot.py` clean and makes it
trivial to extend the bot's vocabulary without touching the core logic.
"""

# ---------------------------------------------------------------------------
# Exit keywords - typing any of these ends the conversation loop.
# ---------------------------------------------------------------------------
EXIT_KEYWORDS = {"exit", "quit", "bye", "goodbye"}

# ---------------------------------------------------------------------------
# Greetings - keyword -> list of possible random replies.
# ---------------------------------------------------------------------------
GREETINGS = {
    "hi": ["Hi there!", "Hi! How can I help you today?", "Hi! Nice to see you."],
    "hello": ["Hello!", "Hello! Nice to meet you.", "Hello there, friend!"],
    "hey": ["Hey!", "Hey there!", "Hey! What's up?"],
    "good morning": ["Good morning! Hope you have a productive day.",
                     "Good morning! ☀️"],
    "good afternoon": ["Good afternoon! How can I help?",
                       "Good afternoon! Hope your day is going well."],
    "good evening": ["Good evening! How was your day?",
                     "Good evening! Nice to chat with you."],
}

# ---------------------------------------------------------------------------
# Introductions - questions about the bot itself.
# ---------------------------------------------------------------------------
INTRODUCTIONS = {
    "who are you": "I am a simple Rule-Based AI Chatbot built in Python.",
    "what is your name": "My name is PyBot - your friendly rule-based assistant.",
    "what can you do": (
        "I can greet you, answer common questions about AI and tech, "
        "tell jokes, share quotes, do basic math, and tell you the time."
    ),
    "who created you": "I was created by a Python developer as a learning project.",
    "what is your purpose": (
        "My purpose is to demonstrate how a rule-based chatbot works "
        "using only Python's if-elif logic and dictionaries."
    ),
}

# ---------------------------------------------------------------------------
# Knowledge base - common factual questions.
# ---------------------------------------------------------------------------
KNOWLEDGE = {
    "what is ai": (
        "Artificial Intelligence (AI) is the simulation of human "
        "intelligence by machines, enabling them to learn, reason, and "
        "make decisions."
    ),
    "what is machine learning": (
        "Machine Learning is a subset of AI that allows systems to learn "
        "patterns from data and improve automatically without being "
        "explicitly programmed."
    ),
    "what is python": (
        "Python is a high-level, interpreted programming language known "
        "for its simple syntax and wide use in AI, web, and data science."
    ),
    "what is data science": (
        "Data Science is the field of extracting insights and knowledge "
        "from structured and unstructured data using statistics, "
        "programming, and domain expertise."
    ),
    "what is chatgpt": (
        "ChatGPT is a conversational AI developed by OpenAI, based on "
        "large language models trained on massive text datasets."
    ),
    "what is deep learning": (
        "Deep Learning is a branch of Machine Learning that uses "
        "multi-layered neural networks to model complex patterns in data."
    ),
}

# ---------------------------------------------------------------------------
# Personal / small-talk conversation.
# ---------------------------------------------------------------------------
SMALL_TALK = {
    "how are you": "I'm just a program, but I'm running smoothly. Thanks for asking!",
    "i am fine": "Glad to hear that! 😊",
    "i'm fine": "Glad to hear that! 😊",
    "thank you": "You're welcome!",
    "thanks": "Anytime! 🙌",
    "nice to meet you": "Nice to meet you too!",
}

# ---------------------------------------------------------------------------
# Random content pools.
# ---------------------------------------------------------------------------
JOKES = [
    "Why do programmers prefer dark mode?\nBecause light attracts bugs!",
    "Why did the developer go broke?\nBecause he used up all his cache.",
    "How many programmers does it take to change a light bulb?\n"
    "None - that's a hardware problem.",
    "Why do Python programmers wear glasses?\nBecause they can't C.",
    "I told my computer I needed a break...\nNow it won't stop sending me KitKat ads.",
]

FUN_FACTS = [
    "Python was named after the comedy group 'Monty Python', not the snake.",
    "The first computer bug was an actual moth found in a Harvard Mark II in 1947.",
    "The first 1GB hard drive (1980) weighed over 500 pounds.",
    "More than 50% of the world's code runs on open-source software.",
    "Octopuses have three hearts - somewhat like distributed systems!",
]

QUOTES = [
    '"The best way to predict the future is to invent it." - Alan Kay',
    '"Talk is cheap. Show me the code." - Linus Torvalds',
    '"Simplicity is the soul of efficiency." - Austin Freeman',
    '"First, solve the problem. Then, write the code." - John Johnson',
    '"Code is like humor. When you have to explain it, it\'s bad." - Cory House',
]

MOTIVATIONS = [
    "Keep going - every expert was once a beginner.",
    "Small steps every day lead to big results. You've got this!",
    "Bugs are just opportunities in disguise. Keep coding!",
    "Discipline beats motivation. Show up, even when it's hard.",
    "Your only competition is who you were yesterday.",
]

# ---------------------------------------------------------------------------
# Fallback responses.
# ---------------------------------------------------------------------------
UNKNOWN_RESPONSE = (
    "I'm sorry, I don't understand that. Please ask another question."
)

WEATHER_RESPONSE = (
    "I'm an offline rule-based chatbot, so I can't access live weather data. "
    "Try a weather website or app for the latest forecast."
)

GOODBYE_RESPONSES = [
    "Goodbye! Have a wonderful day.",
    "Bye! Take care.",
    "See you later! 👋",
]
