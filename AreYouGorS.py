import random
import time

def typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for typing speed
    print()

print("Are you Gay or Straight?")

while True:
    command = input("Press Enter to find out or type 'exit' to quit: ")

    if command.lower() == 'exit':
        break

    word = random.choice(["Gay", "Straight"])
    percentage = random.randint(1, 100)
    emoji = "🌈" if word == "Gay" else "👫"  # Emoji for Gay and Straight

    result_text = f"You are {word} {emoji} at {percentage}%"
    typing_effect(result_text)

print("Thanks for using our service! Goodbye!")
