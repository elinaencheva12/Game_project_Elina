import random

while True:
    computer_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the number guessing game! 🎉")
    print("You have 5 attempts. Good luck! 🍀")

    while True:
        player_input = input("You need to choose a number between 1 and 100: ")
        if not player_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        player_number = int(player_input)
        attempts += 1

        if player_number == computer_number:
            print(f"Congratulations! You chose the right number ({computer_number})! 🎉")
            break
        elif player_number > computer_number:
            print("It's too high.")
        else:
            print("It's too low.")

        if attempts >= 5:
            print(f"Too many attempts! The correct number was {computer_number}. Better luck next time. 😔")
            break

    restart = input("Do you want to play again? 🙂 (yes, no): ").strip().lower()
    if restart != "yes":
        print("Too bad, we'll see each other next time. 😔")
        break




