import random
from move import Result, createMove, Rock, Paper, Scissors

USER_WINNER_MESSAGE = "You Win!"
CPU_WINNER_MESSAGE = "CPU Wins..."
TIE_MESSAGE = "It's a Tie!"
INVALID_INPUT_MESSAGE = "You entered an invalid move"

choices = [Rock(), Paper(), Scissors()]

game_result_messages = {
    Result.TIE: TIE_MESSAGE,
    Result.PLAYER1: USER_WINNER_MESSAGE,
    Result.PLAYER2: CPU_WINNER_MESSAGE,
    Result.INVALID: INVALID_INPUT_MESSAGE
}



def playRound(p1, p2):
    return p1.check(p2)

def getCPUChoice():
    return random.choice(choices)


if __name__ == '__main__':
    user_choice = createMove(input("Welcome to Rock Paper Scissors, please enter your choice: "))
    cpu_choice = getCPUChoice()
    result = playRound(user_choice, cpu_choice)
    print("You chose: {user_choice}, the CPU chose: {cpu_choice}.".format(
        user_choice = user_choice.get_name(), cpu_choice = cpu_choice.get_name()))
    print(game_result_messages[result])