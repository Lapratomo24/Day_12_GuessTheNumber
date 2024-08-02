## Guess the Number ##

logo = '''
    _____                   __  __         _  __           __          
    / ___/_ _____ ___ ___   / /_/ /  ___   / |/ /_ ____ _  / /  ___ ____
    / (_ / // / -_|_-<(_-<  / __/ _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
    \___/\_,_/\__/___/___/  \__/_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   
'''

import os
import random

NORMAL_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def select_difficulty():
    difficulty = input("Select your difficulty: Type 'normal' or 'hard': ")
    if difficulty == 'normal':
        return NORMAL_DIFFICULTY
    elif difficulty == 'hard':
        return HARD_DIFFICULTY

def make_guess(guess, num, turns):
    if guess > num:
        print("Too high.")
        return turns - 1
    elif guess < num:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The right number is {num}.")
        restart()
    
def restart():
    restart = input("Play again? Type 'yes' or 'no': " )
    if restart == 'yes':
        os.system("cls" if os.name == "nt" else "clear")
        start_game()
    else: 
        return

def start_game():
    print("Welcome to Guess the Number game!")
    print("The number will be picked at random and you have several turns to guess it.")
    print("Hint: The number is between 1 and 100.")
    num = random.randint(1, 100)
    print(num)
    
    turns = select_difficulty()
    guess = 0
    while guess != num:
        print(f"You now have {turns} remaining attempts to guess the number.")
        guess = int(input("Guess the number: "))
        turns = make_guess(guess, num, turns)
        if turns == 0:
            print("You ran out of turns. Game over.")
            return
        elif guess != num:
            print("Guess again.")

start_game()


