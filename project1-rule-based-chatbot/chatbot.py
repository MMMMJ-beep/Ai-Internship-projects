# ============================================
# Project 1: Rule-Based Chatbot
# Type: If-Else Logic Chatbot
# Runs in a continuous loop until exit command
# ============================================

import datetime
import random
import sys

def rule_based_chatbot():

    print("=" * 50)
    print("         AI INTERN RULE-BOT v1.0")
    print("   Type 'help' to see what I can do!")
    print("   Type 'exit' or 'bye' to close.")
    print("=" * 50)

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, it's a hardware problem!",
        "A SQL query walks into a bar and asks two tables, 'Can I join you?'",
        "What is a programmer's favorite hangout place? The Foo Bar!"
    ]

    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Your limitation is only your imagination.",
        "Push yourself, because no one else is going to do it for you."
    ]

    try:
        while True:
            user_input = input("\nYou: ").lower().strip()

            # -----------------------------------------
            # 1. Exit Commands
            # -----------------------------------------
            if user_input in ["exit", "bye", "quit", "stop"]:
                print("Bot: It was nice talking to you. Goodbye!")
                break

            # -----------------------------------------
            # 2. Greetings
            # -----------------------------------------
            elif user_input in ["hi", "hello", "hey", "salam"]:
                print("Bot: Hello! How can I assist you today?")

            # -----------------------------------------
            # 3. Time and Date
            # -----------------------------------------
            elif "time" in user_input:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                print(f"Bot: The current time is {current_time}.")

            elif "date" in user_input or "today" in user_input:
                current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                print(f"Bot: Today is {current_date}.")

            # -----------------------------------------
            # 4. Help Command
            # -----------------------------------------
            elif user_input == "help":
                print("Bot: Here is what you can ask me:")
                print("     - 'time' or 'date'")
                print("     - 'tell me a joke'")
                print("     - 'motivate me' or 'quote'")
                print("     - 'what is ai'")
                print("     - 'calculate' or 'math'")
                print("     - 'how are you'")

            # -----------------------------------------
            # 5. AI and Tech Concepts
            # -----------------------------------------
            elif "what is ai" in user_input:
                print("Bot: AI (Artificial Intelligence) is the simulation of human intelligence by machines.")

            elif "python" in user_input:
                print("Bot: Python is a powerful programming language widely used in AI and web development.")

            # -----------------------------------------
            # 6. Jokes and Motivation
            # -----------------------------------------
            elif "joke" in user_input:
                print(f"Bot: {random.choice(jokes)}")

            elif "quote" in user_input or "motivate" in user_input:
                print(f"Bot: {random.choice(quotes)}")

            # -----------------------------------------
            # 7. Basic Math Calculator
            # -----------------------------------------
            elif "calculate" in user_input or "math" in user_input:
                print("Bot: Please type your expression (e.g., 10 + 20):")
                calc = input("Math: ")
                try:
                    result = eval(calc)
                    print(f"Bot: The result is {result}.")
                except Exception:
                    print("Bot: Sorry, I could not calculate that. Please try again.")

            # -----------------------------------------
            # 8. How Are You
            # -----------------------------------------
            elif "how are you" in user_input:
                print("Bot: I am just a program, but I am running perfectly! How about you?")

            # -----------------------------------------
            # 9. Default / Unknown Input
            # -----------------------------------------
            else:
                print("Bot: Sorry, I do not understand that. Type 'help' to see available options.")

    except KeyboardInterrupt:
        print("\nBot: Program interrupted. Allah Hafiz!")
        sys.exit()


if __name__ == "__main__":
    rule_based_chatbot()
