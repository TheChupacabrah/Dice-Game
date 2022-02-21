#Dice Game
#February 14th 2022
#John Hatch

from random import randint
from time import sleep

budget = 100

def get_user_guess(): #function to get user guess
    user_guess = int(input('What number (2-12) do you guess? '))
    print("You chose: " + str(user_guess))
    return user_guess

def roll_dice(wager, budget):  #Function to roll dice
    first_roll = randint(1,6)
    second_roll = randint(1,6)
    total = first_roll + second_roll
    sleep(1)
    user_guess = get_user_guess()

    if wager > budget or wager < 1:
        print("Insufficient Funds")
    elif user_guess > 12 or user_guess < 2:
        print("Guess not valid")
    else:
        print("Rolling Di")
        sleep(2)
        print("The first house roll is " + str(first_roll) + "." )
        sleep(1)
        print("The second house roll is " + str(second_roll) + ".")
        sleep(1)
        print("The house roll is " +str(total) + ".")

    if user_guess == total:
        wager = wager * 12
        print("WOW! You won!")
        return wager

    else:
        print("You lost bozo")
        return -wager
      
#Welcome message
print("Welcome to the BilgeRats Casino!")
#Looping the game
while budget > 0:
    
    choice = input("Would you like to take a stab at the dice game? yes or no? ")
    
    if choice == "no":
        print("Oh really? You best watch your back")
        break
    else:
        print("Great Choice")
        
    
    wager = int(input("How much would you like to wager?  "))
    budget = budget + roll_dice(wager, budget)
    print("Your total is now " + str(budget))
    user_choice = input("Wanna keep playing? Press enter, if not, press q")
    if user_choice == "q":
        print("you ended with" + str(budget) + "dollars")
        break
    if budget == 0:
        print("Leave with your broke ass")
        break
    
    
