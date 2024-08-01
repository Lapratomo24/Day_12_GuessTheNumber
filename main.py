## Guess the Number ##

logo = '''
    _____                   __  __         _  __           __          
    / ___/_ _____ ___ ___   / /_/ /  ___   / |/ /_ ____ _  / /  ___ ____
    / (_ / // / -_|_-<(_-<  / __/ _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
    \___/\_,_/\__/___/___/  \__/_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   
'''

import os
import random

def difficulty_selection(difficulty):
    
    nums = list(range(1, 101)) # randint(1,100) alternatively
    random_num = random.choice(nums)
    print(f"Number is {random_num}")
    
    if difficulty == 'beginner':
        attempts = 10
    elif difficulty == 'advanced':
        attempts = 5
        
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
            
        if guess == random_num:
            print("You got the right number! Congrats!")
            restart = input("Play again? Type 'yes' or 'no': " )
            if restart == 'yes':
                os.system("cls" if os.name == "nt" else "clear")
                difficulty_selection(difficulty)
            elif restart == 'no': 
                return
            
        elif guess < random_num:
            print("Too low.")
            print("Guess again.")
        else:
            print("Too high.")
            print("Guess again.")
            
        if attempts == 0:
            print(f"You ran out of turns. The number is {random_num}.")
        else:
            print(f"You have {attempts} attempts remaining.")
            
# while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': " ) == 'yes':
#     os.system("cls" if os.name == "nt" else "clear")
#     difficulty_selection()

print("")
print("Welcome to Guess the Number game!")
print("We pick a number for you to guess. What's your difficulty?")
difficulty = input("Choose between 'beginner' and 'advanced': ")

difficulty_selection(difficulty)