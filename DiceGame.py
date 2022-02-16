#Dice Game
#February 14th 2022
#John Hatch

from random import randint
from time import sleep

def get_user_guess():
    user_guess = int(input('What number (2-12) do you guess? '))
    print("You chose: " + str(user_guess))
    return user_guess

def roll_dice():
    first_roll = randint(1,6)
    second_roll = randint(1,6)
    total = first_roll + second_roll
    user_guess = get_user_guess()

    if user_guess > 12 and user_guess < 2:
        print("Choose a correct number")
    
    else:
        print("Rolling Di")
        sleep(1)
        print("The first roll is " + str(first_roll))
        sleep(1)
        print("The second roll is " + str(second_roll))
        sleep(1)
        print("The house roll is " +str(first_roll + second_roll))

    if user_guess == total:
        print("WOW! You won!")

    else:
        print("You lost bozo")
roll_dice()      
    
    