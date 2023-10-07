import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I've selected a random number between 1 and 10. Try to guess it.")
    print("Type 'exit' to quit the game.")

    while True:
        user_input = input("Enter your guess: ")

        if user_input.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        try:
            user_guess = int(user_input)
            attempts += 1

            if user_guess < secret_number:
                print("Try a higher number.")
            elif user_guess > secret_number:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

if __name__ == "__main__":
    guess_the_number()
