# --- Pro Guess the Number Game for GKS Prep Portfolio ---
import random

def play_game():
    print("\n=============================================")
    print("🎲 WELCOME TO THE NUMBER GUESSING GAME 🚀")
    print("=============================================")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")
    print("=============================================")

    # Computer will select a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("\nEnter your guess between 1 and 100: "))
        except ValueError:
            print("❌ Invalid Input! Please enter numbers only.")
            continue

        attempts += 1  # Count every attempt

        if user_guess < 1 or user_guess > 100:
            print("⚠ Out of Range! Please enter a number between 1 and 100.")
        elif user_guess < secret_number:
            print("📉 Too Low! Try a higher number.")
        elif user_guess > secret_number:
            print("📈 Too High! Try a lower number.")
        else:
            print(f"\n🎉 CONGRATULATIONS! You guessed the correct number! 🥳")
            print(f"🏆 You guessed the number in {attempts} attempts.")
            break


# Run the game
if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()

        if replay != 'y':
            print("\nThanks for playing! Keep building your portfolio. Annyeong! 👋")
            break
