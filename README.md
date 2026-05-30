# Rule-Based AI Chatbot 🤖

## 📌 Project Overview

This chatbot is a simple rule-based AI assistant built using Python.  
It responds to predefined user inputs using conditional logic (`if-elif-else`) and runs continuously until the user exits the program.

The project demonstrates the fundamentals of:
- Control Flow
- Decision-Making Logic
- Input Processing
- Rule-Based Artificial Intelligence

---

## 🚀 Features

- Greeting detection
- Exit commands
- Input cleaning and preprocessing
- Continuous chatbot conversation loop
- Randomized responses
- Help command
- Basic conversational abilities

---

## 🧠 Supported Commands

The chatbot can currently respond to:

- Greetings
  - hi
  - hello
  - hey

- Questions
  - how are you
  - what is your name
  - what can you do / your capabilities
  - what is decodelabs

- Other Commands
  - help
  - thanks
  - decodelabs

- Exit Commands
  - bye
  - goodbye
  - exit
  - quit

---

## 📂 Project Structure

```text
Task-1-MariamAhmed/
│
├── main.py          # Entry point — runs the chatbot loop
├── response.py      # Core logic — intent matching and responses
├── utils.py         # Input sanitization (clean_input function)
├── README.md        # Project documentation
└── requirements.txt # Dependencies (none required beyond standard library)

==============================================

## ▶️ How to Run

1. **Clone or Download the Repository**
```bash
   git clone https://github.com/your-username/Task-1-MariamAhmed.git
```

2. **Navigate to the Project Folder**
```bash
   cd RuleBasedBot
```

3. **Run the Program**
```bash
   python main.py
```

> No external libraries required. Built entirely with Python's standard library.

---

## 💡 Example Interaction
Welcome! I am DecodeBot.
Type 'bye' or 'exit' to quit.
You: Hello!
Bot: Hi! How can I help you?
You: How are you?
Bot: All systems running perfectly!
You: What is DecodeLabs?
Bot: DecodeLabs is a training platform for AI and software engineering internships.
You: bye
Bot: Goodbye! It was nice talking to you.
