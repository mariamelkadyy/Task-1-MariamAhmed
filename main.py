from response import get_response
from utils import clean_input
from response import EXIT_WORDS

print("Bot: Welcome! I am DecodeBot.")
print("Bot: Type 'bye' to exit.")
print('=' * 20)

while True:
    user_input = input("You: ").strip()

    if not user_input:
        print("Bot: Please type something!\n")
        continue

    cleaned_input = clean_input(user_input)
    response = get_response(cleaned_input)
    print(f"Bot: {response}\n")

    if cleaned_input in ["bye", "exit", "quit"]:
        break