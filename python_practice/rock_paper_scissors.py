#A little game of Rock Paper Scisors.
valid_i = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

def validation(player):
    try:
        election = raw_input("What is your choice player " + player + "?").upper()
        if election in valid_i.values():
            print("got it!")
        else:
            raise Exception ('ValueError')
    except Exception as error:
        print("wrong election, please enter a valid election")
        validation(player)
    return election

def winner(ch1, ch2):
    keys = valid_i.keys()
    values = valid_i.values()
    ch1 = keys[values.index(ch1)]
    ch2 = keys[values.index(ch2)]

    result = ch1 - ch2
    print "Processing..."
    if result == -2 or result == 1:
        print "Won player 1"
    elif result == 0:
        print "it's a tie"
    else:
        print "Won player 2"

    active = False



p1_choice = validation("1")
p2_choice = validation("2")

winner(p1_choice, p2_choice)

# rock > SCISSORS
# paper > Rock
# scissors > Paper 3 11 19
#
# 1 > 3
# 2 > 1
# 3 > 2

-2, 1, 1
2, -1, -1
