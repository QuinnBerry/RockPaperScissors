import random

TIE = "tie"
PLAYER1 = "player1"
PLAYER2 = "player2"
INVALID_INPUT = "invalid input"

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

choices = [ROCK, PAPER, SCISSORS]



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

def getCPUChoice():
    return random.choice(choices)


if __name__ == '__main__':
    user_choice = input("Welcome to Rock Paper Scissors, please enter your choice: ")
    cpu_choice = getCPUChoice()
    result = playRound(user_choice, cpu_choice)
    print("You chose: {user_choice}, the CPU chose: {cpu_choice}.".format(
        user_choice = user_choice.capitalize(), cpu_choice = cpu_choice.capitalize()))
    print("{result} wins!".format(result = result.capitalize()))