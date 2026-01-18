import datetime
import random
import time

def print_slowly(text):
    """Adds a realistic typing effect to the chatbot."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def get_time_of_day():
    """Returns a greeting based on the current hour."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def chatbot_v2():
    # --- Data Lists (To increase complexity and functionality) ---
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Real programmers count from 0.",
        "Why did the developer go broke? Because he used up all his cache."
    ]
    
    quotes = [
        "First, solve the problem. Then, write the code. – John Johnson",
        "Code is like humor. When you have to explain it, it’s bad. – Cory House",
        "Knowledge is power. – Francis Bacon",
        "The only way to do great work is to love what you do. – Steve Jobs"
    ]

    greetings = ["hi", "hello", "hey", "hola", "greetings"]
    farewells = ["bye", "exit", "quit", "goodbye", "see you"]
    
    # --- Initialization ---
    user_name = "User"
    is_running = True
    
    print("="*50)
    print_slowly(f"Chatbot: {get_time_of_day()}! I am your Advanced Python Assistant.")
    print_slowly("Chatbot: I can tell jokes, give quotes, do math, or just chat.")
    print("="*50)

    # --- Main Loop ---
    while is_running:
        user_input = input(f"\n[{user_name}]: ").strip().lower()

        # 1. Exit Logic
        if any(word in user_input for word in farewells):
            print_slowly(f"Chatbot: It was nice talking to you, {user_name}! Have a great day.")
            is_running = False

        # 2. Name Personalization
        elif "my name is" in user_input:
            name_parts = user_input.split("is")
            user_name = name_parts[-1].strip().capitalize()
            print_slowly(f"Chatbot: Pleased to meet you, {user_name}!")

        elif "what is my name" in user_input:
            print_slowly(f"Chatbot: Your name is {user_name}.")

        # 3. Greetings
        elif any(word in user_input for word in greetings):
            print_slowly(f"Chatbot: {random.choice(['Hello!', 'Hi there!', 'Hey!'])} How can I help you today?")

        # 4. Identity Questions
        elif "who are you" in user_input or "what is your name" in user_input:
            print_slowly("Chatbot: I am a Task 4 Python Chatbot created for the CodeAlpha Internship.")

        # 5. Status/Mood
        elif "how are you" in user_input:
            print_slowly("Chatbot: I'm functioning at 100% efficiency! Thank you for asking. How are you feeling?")
            
        elif "happy" in user_input or "good" in user_input or "fine" in user_input:
            print_slowly("Chatbot: That is wonderful to hear! Positive vibes only.")
            
        elif "sad" in user_input or "bad" in user_input or "tired" in user_input:
            print_slowly("Chatbot: I'm sorry to hear that. Maybe a joke would cheer you up? Type 'joke'.")

        # 6. Time and Date
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print_slowly(f"Chatbot: The current time is {now}.")

        elif "date" in user_input:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            print_slowly(f"Chatbot: Today's date is {today}.")

        # 7. Entertainment (Jokes/Quotes)
        elif "joke" in user_input:
            print_slowly(f"Chatbot: Here is a funny one: {random.choice(jokes)}")

        elif "quote" in user_input:
            print_slowly(f"Chatbot: Think about this: {random.choice(quotes)}")

        # 8. Math Capabilities
        elif "calculate" in user_input or "math" in user_input:
            print_slowly("Chatbot: I can do basic math. Enter the first number:")
            try:
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                op = input("Operation (+, -, *, /): ")
                
                if op == '+': result = num1 + num2
                elif op == '-': result = num1 - num2
                elif op == '*': result = num1 * num2
                elif op == '/': result = num1 / num2 if num2 != 0 else "Error (Div by zero)"
                else: result = "Invalid operator"
                
                print_slowly(f"Chatbot: The result is {result}")
            except ValueError:
                print_slowly("Chatbot: Please enter valid numbers.")

        # 9. Python Facts
        elif "python" in user_input:
            print_slowly("Chatbot: Python was created by Guido van Rossum and released in 1991.")

        # 10. Help Menu
        elif "help" in user_input:
            print("\n--- Command Menu ---")
            print("1. Greetings (Hi, Hello)")
            print("2. Set name (My name is...)")
            print("3. Time/Date")
            print("4. Entertainment (Joke, Quote)")
            print("5. Math (Calculate)")
            print("6. Exit (Bye)")

        # 11. Fallback Response
        else:
            print_slowly("Chatbot: I'm not sure I understand that. Type 'help' to see what I can do.")

# Entry point
if __name__ == "__main__":
    chatbot_v2()