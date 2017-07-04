#A little game of Rock Paper Scisors.
active = True
valid_i = {'1': "ROCK", '2': "PAPER", '3': "SCISSORS"}

def validation(player):
    try:
        election = raw_input("What is your choice player " + player + "?")
        if election in valid_i.values():
            print("got it!")
        else:
            raise Exception ('ValueError')
    except Exception as error:
        print("wrong election, please enter a valid election")
        validation(player)


while active:
    validation("1")
    validation("2")
