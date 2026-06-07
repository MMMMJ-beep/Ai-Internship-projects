# Project 1: Rule-Based Chatbot

## Overview
A simple rule-based chatbot built using Python that responds to predefined user inputs using if-else logic and runs in a continuous loop.

---

## Goal
Create a chatbot that handles greetings, exit commands, and various user queries using control flow and decision-making logic.

---

## Project Structure
```
project1-rule-based-chatbot/
│
├── chatbot.py         # Main chatbot script
├── requirements.txt   # Required libraries
└── README.md          # Project documentation
```

---

## Features
| Command | Response |
|--------|----------|
| hi, hello, hey, salam | Greeting response |
| exit, bye, quit, stop | Exits the chatbot |
| time | Current time |
| date / today | Current date |
| help | Lists available commands |
| what is ai | AI definition |
| python | Python description |
| joke | Random programming joke |
| motivate / quote | Random motivational quote |
| calculate / math | Basic math calculator |
| how are you | Status response |

---

## Key Skills Used
- Control flow with if-else logic
- Continuous loop with while True
- String matching and input handling
- Python datetime and random modules
- Basic AI concepts (rule-based systems)

---

## How to Run
```bash
python chatbot.py
```

No external libraries required. Uses Python standard library only.

---

## Sample Interaction
```
You: hello
Bot: Hello! How can I assist you today?

You: what is ai
Bot: AI (Artificial Intelligence) is the simulation of human intelligence by machines.

You: joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
Bot: It was nice talking to you. Goodbye!
```
