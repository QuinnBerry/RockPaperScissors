import unittest
import game
from move import Result, createMove, ROCK, PAPER, SCISSORS

class TestGame(unittest.TestCase):
    def test_rock_vs_rock(self): 
        self.assertEqual(Result.TIE, game.playRound(createMove(ROCK), createMove(ROCK)))

    def test_rock_vs_paper(self):
        self.assertEqual(Result.PLAYER2, game.playRound(createMove(ROCK), createMove(PAPER)))

    def test_rock_vs_scissors(self):
        self.assertEqual(Result.PLAYER1, game.playRound(createMove(ROCK), createMove(SCISSORS)))

    def test_paper_vs_paper(self):
        self.assertEqual(Result.TIE, game.playRound(createMove(PAPER), createMove(PAPER)))
    
    def test_paper_vs_rock(self):
        self.assertEqual(Result.PLAYER1, game.playRound(createMove(PAPER), createMove(ROCK)))
    
    def test_paper_vs_scissors(self):
        self.assertEqual(Result.PLAYER2, game.playRound(createMove(PAPER), createMove(SCISSORS)))

    def test_scissors_vs_scissors(self):
        self.assertEqual(Result.TIE, game.playRound(createMove(SCISSORS), createMove(SCISSORS)))

    def test_scissors_vs_paper(self):
        self.assertEqual(Result.PLAYER1, game.playRound(createMove(SCISSORS), createMove(PAPER)))
    
    def test_scissors_vs_rock(self):
        self.assertEqual(Result.PLAYER2, game.playRound(createMove(SCISSORS), createMove(ROCK)))
    
    def test_invalid_input(self):
        self.assertEqual(Result.INVALID, game.playRound(createMove("invalid"), createMove(SCISSORS)))
        self.assertEqual(Result.INVALID, game.playRound(createMove(SCISSORS), createMove("invalid")))

if __name__ == '__main__':
    unittest.main()