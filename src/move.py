from enum import Enum

class Result(Enum):
    PLAYER1 = 1
    PLAYER2 = 2
    TIE = 3
    INVALID = 4

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

def createMove(moveType):
    if moveType.casefold() == ROCK:
        return Rock()
    elif moveType.casefold() == PAPER:
        return Paper()
    elif moveType.casefold() == SCISSORS:
        return Scissors()
    else:
        return Invalid()

class Move():
    def check(self, move):
        pass
    def get_name(self):
        return type(self).__name__

class Rock(Move):
    def check(self, move):
        if isinstance(move, Rock):
            return Result.TIE
        elif isinstance(move, Scissors):
            return Result.PLAYER1
        elif isinstance(move, Paper):
            return Result.PLAYER2
        else:
            return Result.INVALID

class Paper(Move):
    def check(self, move):
        if isinstance(move, Paper):
            return Result.TIE
        elif isinstance(move, Rock):
            return Result.PLAYER1
        elif isinstance(move, Scissors):
            return Result.PLAYER2
        else:
            return Result.INVALID

class Scissors(Move):
    def check(self, move):
        if isinstance(move, Scissors):
            return Result.TIE
        elif isinstance(move, Paper):
            return Result.PLAYER1
        elif isinstance(move, Rock):
            return Result.PLAYER2
        else:
            return Result.INVALID
        
class Invalid(Move):
    def check(self, move):
        return Result.INVALID
