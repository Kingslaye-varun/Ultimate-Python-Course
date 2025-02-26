import random

# Define the choices
choices = ["snake", "water", "gun"]

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a Draw! 🤝"
    
    # Winning conditions
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You Win! 🎉"
    else:
        return "Computer Wins! 😢"

# Main game loop
while True:
    print("\nChoices: Snake, Water, Gun")
    user_choice = input("Enter your choice: ").strip().lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        continue
    
    # Computer's random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine and print the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
