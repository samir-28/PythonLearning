import numpy as np

def get_user_choice():
    User = input("Please enter your choice (rock, paper, or scissors): ").lower()
    return User

def get_computer_choice():
    choices = np.array(['rock', 'paper', 'scissors'])
    return np.random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if ((user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
        
        print("You won! You know computer can defeat God...")
        
    elif user_choice == computer_choice:
        print("Game tied!Tough match...")
    else: 
        print("Computer won!You loose -> Once a losser always a looser... !")

def play_game():
    print("Let's begin the battle!")
    user = get_user_choice()
    computer = get_computer_choice()
    print("User choice is:", user)
    print("Computer choice is:", computer)
    determine_winner(user, computer)

play_game()
