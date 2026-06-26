"""
chatbot.py
----------
Rule-Based AI Chatbot - main entry point.

A professional, modular rule-based chatbot built with pure Python.
No machine-learning models or external AI APIs are used; all responses
are produced through deterministic if-elif logic and dictionary lookups
defined in `responses.py`.

Bonus features included:
    * Random greetings, jokes, quotes, fun facts, motivations
    * Conversation history saved to `chat_history.txt`
    * Colored terminal output via `colorama` (graceful fallback if missing)
    * Typing animation for a more natural feel
    * Safe arithmetic calculator
    * Current date and time lookup
"""

from __future__ import annotations

import datetime
import random
import re
import sys
import time
from pathlib import Path
from typing import List, Optional

from responses import (
    EXIT_KEYWORDS,
    GREETINGS,
    INTRODUCTIONS,
    KNOWLEDGE,
    SMALL_TALK,
    JOKES,
    FUN_FACTS,
    QUOTES,
    MOTIVATIONS,
    UNKNOWN_RESPONSE,
    WEATHER_RESPONSE,
    GOODBYE_RESPONSES,
)

# ---------------------------------------------------------------------------
# Optional color support (colorama). Falls back to plain text if unavailable.
# ---------------------------------------------------------------------------
try:
    from colorama import Fore, Style, init as _colorama_init

    _colorama_init(autoreset=True)
    C_BOT = Fore.CYAN + Style.BRIGHT
    C_USER = Fore.GREEN + Style.BRIGHT
    C_SYS = Fore.YELLOW + Style.BRIGHT
    C_ERR = Fore.RED + Style.BRIGHT
    C_RESET = Style.RESET_ALL
except ImportError:  # pragma: no cover - cosmetic fallback only
    C_BOT = C_USER = C_SYS = C_ERR = C_RESET = ""


# Conversation history kept in memory and flushed to disk on exit.
HISTORY: List[str] = []
HISTORY_FILE = Path(__file__).parent / "chat_history.txt"


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------
def type_out(text: str, delay: float = 0.015) -> None:
    """Print text with a small typing animation for a friendlier feel."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def bot_say(message: str) -> None:
    """Print a bot message with color + typing animation and log it."""
    sys.stdout.write(f"{C_BOT}Bot:{C_RESET} ")
    type_out(message)
    HISTORY.append(f"Bot: {message}")


def banner() -> None:
    """Display the welcome banner."""
    line = "=" * 40
    print(f"{C_SYS}{line}")
    print(f"{C_SYS}        RULE BASED AI CHATBOT")
    print(f"{C_SYS}{line}{C_RESET}\n")
    bot_say("Hello! I am your AI chatbot.")
    bot_say("Type 'exit', 'quit', or 'bye' anytime to leave.\n")


# ---------------------------------------------------------------------------
# Intent handlers
# ---------------------------------------------------------------------------
def greeting_response(user_input: str) -> Optional[str]:
    """Return a random greeting reply if user_input contains a greeting."""
    for key, replies in GREETINGS.items():
        if key in user_input:
            return random.choice(replies)
    return None


def introduction_response(user_input: str) -> Optional[str]:
    """Match introduction-style questions."""
    for key, reply in INTRODUCTIONS.items():
        if key in user_input:
            return reply
    return None


def knowledge_response(user_input: str) -> Optional[str]:
    """Match common factual questions from the knowledge base."""
    for key, reply in KNOWLEDGE.items():
        if key in user_input:
            return reply
    return None


def small_talk_response(user_input: str) -> Optional[str]:
    """Handle personal / small-talk style messages."""
    for key, reply in SMALL_TALK.items():
        if key in user_input:
            return reply
    return None


def fun_response(user_input: str) -> Optional[str]:
    """Handle jokes, fun facts, quotes, and motivational requests."""
    if "joke" in user_input:
        return random.choice(JOKES)
    if "fun fact" in user_input or "fact" in user_input:
        return random.choice(FUN_FACTS)
    if "quote" in user_input:
        return random.choice(QUOTES)
    if "motivate" in user_input or "motivation" in user_input:
        return random.choice(MOTIVATIONS)
    return None


def date_time(user_input: str) -> Optional[str]:
    """Return current date and/or time when asked."""
    now = datetime.datetime.now()
    if "date" in user_input and "time" in user_input:
        return now.strftime("Today is %A, %B %d, %Y and the time is %H:%M:%S.")
    if "date" in user_input or "day" in user_input:
        return now.strftime("Today's date is %A, %B %d, %Y.")
    if "time" in user_input:
        return now.strftime("The current time is %H:%M:%S.")
    return None


def weather_response(user_input: str) -> Optional[str]:
    """Politely decline weather-related requests (no live API)."""
    if "weather" in user_input or "temperature" in user_input or "forecast" in user_input:
        return WEATHER_RESPONSE
    return None


# ---------------------------------------------------------------------------
# Calculator
# ---------------------------------------------------------------------------
# Match an expression that uses only digits, operators, parentheses,
# decimal points, and whitespace. This prevents `eval` from running
# arbitrary Python code.
_CALC_PATTERN = re.compile(r"^[\d\s+\-*/().]+$")


def calculator(user_input: str) -> Optional[str]:
    """Safely evaluate a basic arithmetic expression.

    Triggered by inputs starting with the word 'calculate' or 'calc',
    e.g. `calculate 25 + 15` or `calc 100 / 4`.
    """
    triggers = ("calculate", "calc ", "compute")
    if not any(user_input.startswith(t) for t in triggers):
        return None

    # Strip the trigger word and any surrounding whitespace.
    expression = user_input
    for t in triggers:
        if expression.startswith(t):
            expression = expression[len(t):].strip()
            break

    if not expression:
        return "Please provide an expression, e.g. `calculate 25 + 15`."

    if not _CALC_PATTERN.match(expression):
        return "Sorry, I can only evaluate numbers and + - * / ( ) operators."

    try:
        # `eval` is sandboxed: no builtins and no globals/locals exposed.
        result = eval(expression, {"__builtins__": {}}, {})  # noqa: S307
    except ZeroDivisionError:
        return "Math error: division by zero."
    except Exception:
        return "Sorry, I couldn't evaluate that expression."

    return f"{expression} = {result}"


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------
# Order matters: more specific matchers should run before generic ones.
HANDLERS = (
    calculator,
    date_time,
    weather_response,
    introduction_response,
    knowledge_response,
    fun_response,
    small_talk_response,
    greeting_response,
)


def get_response(user_input: str) -> str:
    """Run the input through each handler and return the first match."""
    cleaned = user_input.lower().strip()
    for handler in HANDLERS:
        reply = handler(cleaned)
        if reply:
            return reply
    return UNKNOWN_RESPONSE


# ---------------------------------------------------------------------------
# History persistence
# ---------------------------------------------------------------------------
def save_history() -> None:
    """Append the current session's conversation to chat_history.txt."""
    if not HISTORY:
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with HISTORY_FILE.open("a", encoding="utf-8") as fh:
        fh.write(f"\n--- Session {timestamp} ---\n")
        fh.write("\n".join(HISTORY))
        fh.write("\n")


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def main() -> None:
    """Run the chatbot's interactive conversation loop."""
    banner()

    while True:
        try:
            user_input = input(f"{C_USER}You:{C_RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            bot_say(random.choice(GOODBYE_RESPONSES))
            break

        # Input validation - ignore empty submissions.
        if not user_input:
            bot_say("Please type something so I can help.")
            continue

        HISTORY.append(f"You: {user_input}")

        # Check for exit keywords first.
        if user_input.lower() in EXIT_KEYWORDS:
            bot_say(random.choice(GOODBYE_RESPONSES))
            break

        # Generate and display the bot's reply.
        reply = get_response(user_input)
        bot_say(reply)

    save_history()


if __name__ == "__main__":
    main()
