# Number Guessing Game with High Score Tracker

# Features:
# - Random number guessing
# - Multiple levels of difficulty
# - Keeps track of best score
# - Menu-driven with exit option
 
import random
 
# Global variable for best score
best_score = None
 
def show_menu():
    """Display main menu"""
    print("\n=== Number Guessing Game ===")
    print("1. Play Game")
    print("2. Show Best Score")
    print("3. Help")
    print("4. Exit")
 
def get_choice():
    """Get a valid menu choice"""
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice. Please select 1-4.")
 
def choose_difficulty():
    """Choose difficulty level"""
    print("\nSelect Difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print("4. Extreme (1-500)")
    while True:
        level = input("Enter difficulty (1-4): ")
        if level == "1":
            return 1, 10
        elif level == "2":
            return 1, 50
        elif level == "3":
            return 1, 100
        elif level == "4":
            return 1, 500
        else:
            print("Invalid choice. Please select 1-4.")
 
def play_game():
    """Play one round of the game"""
    global best_score
    low, high = choose_difficulty()
    secret = random.randint(low, high)
    attempts = 0
 
    print(f"\nI have chosen a number between {low} and {high}. Can you guess it?")
 
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("🎉 New Best Score! 🎉")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
 
def show_best_score():
    """Display the best score so far"""
    if best_score is None:
        print("\nNo games played yet.")
    else:
        print(f"\nBest score so far: {best_score} attempts")
 
def show_help():
    """Display help instructions"""
    print("\n--- Help ---")
    print("1. Choose 'Play Game' to start guessing.")
    print("2. Select a difficulty level (Easy to Extreme).")
    print("3. Enter your guesses until you find the correct number.")
    print("4. Try to beat your best score in fewer attempts!")
    print("5. Use 'Show Best Score' to view your record.")
    print("6. Choose 'Exit' to quit the game.")
 
def main():
    """Main loop for the game"""
    while True:
        show_menu()
        choice = get_choice()
 
        if choice == "1":
            play_game()
        elif choice == "2":
            show_best_score()
        elif choice == "3":
            show_help()
        elif choice == "4":
            print("Thank you for playing! Goodbye!")
            break
 
# Entry point
if __name__ == "__main__":
    main()
 