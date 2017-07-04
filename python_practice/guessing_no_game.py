#A two player game about guessing a number.
import random

CONST_RANGE = 101
active = True
computer_election = 0

def validation(player):
    try:
        print("Guess the number " + str(player))
        print("Choice a number between 0 and " + str(CONST_RANGE - 1))
        election = input("What is your choice ?")
        if type(election) is int:
            print("got it!")
        else:
            raise Exception ('ValueError')
    except Exception as error:
        print("Please enter a number")
        validation(player)

computer_election = random.randrange(CONST_RANGE)
validation(1)
validation(2)
