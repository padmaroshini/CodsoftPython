from flask import Blueprint
import random

auth = Blueprint('auth', __name__)

@auth.route('/cal')  
def cal():
    return 'cal'

def play_game():
    print("Welcome to Stone, Paper, Scissors!")
    choices = ["stone", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter your choice (stone, paper, scissors or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        print()

if __name__ == "__main__":
    play_game()
