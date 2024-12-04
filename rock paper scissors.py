import random
print("welcome to a rock paper scissors game")
def play_game():
    options = ["rock", "paper", "scissors"]
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice, bruv! Try again.")
        return
    
    computer_choice = random.choice(options)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win, champ!")
    else:
        print("Computer wins, better luck next time!")

if __name__ == "__main__":
    play_game()
