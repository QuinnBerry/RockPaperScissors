
TIE = "tie"
PLAYER1 = "player1"
PLAYER2 = "player2"
INVALID_INPUT = "invalid input"
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"


def playRound(p1, p2):
    if (p1.casefold() == p2.casefold()):
        return TIE
    elif (p1.casefold() == ROCK and p2.casefold() == PAPER):
        return PLAYER2
    elif (p1.casefold() == ROCK and p2.casefold() == SCISSORS):
        return PLAYER1
    elif (p1.casefold() == PAPER and p2.casefold() == ROCK):
        return PLAYER1
    elif(p1.casefold() == PAPER and p2.casefold() == SCISSORS):
        return PLAYER2
    elif(p1.casefold() == SCISSORS and p2.casefold() == PAPER):
        return PLAYER1
    elif(p1.casefold() == SCISSORS and p2.casefold() == ROCK):
        return PLAYER2
    else:
        return INVALID_INPUT