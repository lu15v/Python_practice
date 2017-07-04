#A two player game about guessing a number.
import random

CONST_RANGE = 101
active = True
computer_election = 0
players = [1, 2]
choice = []
def validation(player):
    try:
        print("Guess the number player " + str(player))
        print("Choice a number between 0 and " + str(CONST_RANGE - 1))
        election = input("What is your choice ?")
        if type(election) is int:
            print("got it!")
        else:
            raise Exception ('ValueError')
    except Exception as error:
        print("Please enter a number")
        validation(player)
    return election

def orientation(number):
    if number > computer_election:
        print("Your number is over the correct one, try again")
    elif number < computer_election:
        print("Your number is below the correct one, try again")
    else:
        print("That is the number, you win!")
        print("Game Over")


computer_election = random.randrange(CONST_RANGE)
print computer_election
while active:
    for p in players:
        choice.append(validation(p))
        orientation(choice[p -1])
        if choice[p - 1] == computer_election:
            active = False
            break
