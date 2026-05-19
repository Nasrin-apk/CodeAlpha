import datetime
import random

# -----------------------------------
# INTRO
# -----------------------------------

print("=" * 60)
print("🤖 ADVANCED SMART CHATBOT")
print("=" * 60)

print("Type 'help' to see commands")
print("Type 'bye' to exit")

# -----------------------------------
# QUOTES
# -----------------------------------

quotes = [
    "Success comes from hard work.",
    "Never stop learning.",
    "Believe in yourself.",
    "Practice makes perfect.",
    "Dream big and achieve big."
]

# -----------------------------------
# CHAT LOOP
# -----------------------------------

while True:

    user = input("\n🗨 You: ").lower()

    # -----------------------------------

    if user == "hello":

        print("🤖 Bot: Hello! Nice to meet you.")

    # -----------------------------------

    elif user == "how are you":

        print("🤖 Bot: I am doing great!")

    # -----------------------------------

    elif user == "your name":

        print("🤖 Bot: My name is Advanced Python Chatbot")

    # -----------------------------------

    elif user == "time":

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print("⏰ Current Time:", current_time)

    # -----------------------------------

    elif user == "date":

        today = datetime.date.today()

        print("📅 Today's Date:", today)

    # -----------------------------------

    elif user == "quote":

        print("💡 Motivational Quote:")

        print(random.choice(quotes))

    # -----------------------------------

    elif user == "calculator":

        try:

            num1 = float(input("Enter first number: "))

            num2 = float(input("Enter second number: "))

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = int(input("Choose operation: "))

            if choice == 1:

                print("✅ Result:", num1 + num2)

            elif choice == 2:

                print("✅ Result:", num1 - num2)

            elif choice == 3:

                print("✅ Result:", num1 * num2)

            elif choice == 4:

                print("✅ Result:", num1 / num2)

            else:

                print("❌ Invalid Choice")

        except:

            print("❌ Error occurred")

    # -----------------------------------

    elif user == "help":

        print("\n" + "=" * 40)

        print("📋 AVAILABLE COMMANDS")

        print("=" * 40)

        print("hello")
        print("how are you")
        print("your name")
        print("time")
        print("date")
        print("quote")
        print("calculator")
        print("bye")

    # -----------------------------------

    elif user == "bye":

        print("👋 Bot: Goodbye!")

        break

    # -----------------------------------

    else:

        print("❌ Bot: Command not found")