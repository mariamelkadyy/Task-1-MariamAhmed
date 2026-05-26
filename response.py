import random

EXIT_WORDS = ["bye", "goodbye", "exit", "quit"]

def get_response(user):

    if any(word in user for word in ["hi", "hello", "hey"]):
        return "Hi! How can I help you?"

    elif any(word in user for word in EXIT_WORDS):
        return "Goodbye!"

    elif "how are you" in user:
        responses = [
            "I'm doing great!",
            "I'm good, thanks for asking!",
            "All systems running perfectly!"
        ]
        return random.choice(responses)

    elif "your name" in user or "name" in user:
        return "My name is DecodeBot, your rule-based assistant."

    elif "help" in user:
        return "You can greet me, ask how I am, ask my name, or say bye"

    elif "decodelabs" in user:
        return "DecodeLabs is a training platform for AI and software engineering internships"

    elif "what can you do" in user or "capabilities" in user:
        return "I can answer greetings, tell you my name, and chat about DecodeLabs!"

    elif "thank" in user:
        return "You're welcome! Happy to help."
    else:
        return "Sorry, I can't understand that yet, Try asking for 'help'."