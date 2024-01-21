import random

TIE = "tie"
PLAYER1 = "player1"
PLAYER2 = "player2"
INVALID_INPUT = "invalid input"

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

USER_WINNER_MESSAGE = "You Win!"
CPU_WINNER_MESSAGE = "CPU Wins..."
TIE_MESSAGE = "It's a Tie!"
INVALID_INPUT_MESSAGE = "You entered an invalid move"

choices = [ROCK, PAPER, SCISSORS]

game_result_messages = {
    TIE: TIE_MESSAGE,
    PLAYER1: USER_WINNER_MESSAGE,
    PLAYER2: CPU_WINNER_MESSAGE,
    INVALID_INPUT: INVALID_INPUT_MESSAGE
}



def playRound(p1, p2):
    return p1.check(p2)

def getCPUChoice():
    return random.choice(choices)


if __name__ == '__main__':
    user_choice = input("Welcome to Rock Paper Scissors, please enter your choice: ")
    cpu_choice = getCPUChoice()
    result = playRound(user_choice, cpu_choice)
    print("You chose: {user_choice}, the CPU chose: {cpu_choice}.".format(
        user_choice = user_choice.capitalize(), cpu_choice = cpu_choice.capitalize()))
    print(game_result_messages[result])