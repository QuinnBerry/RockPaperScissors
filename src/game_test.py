import unittest
import game

class TestGame(unittest.TestCase):
    def test_rock_vs_rock(self): 
        self.assertEqual(game.TIE, game.playRound(game.ROCK, game.ROCK))

    def test_rock_vs_paper(self):
        self.assertEqual(game.PLAYER2, game.playRound(game.ROCK, game.PAPER))

    def test_rock_vs_scissors(self):
        self.assertEqual(game.PLAYER1, game.playRound(game.ROCK, game.SCISSORS))

    def test_paper_vs_paper(self):
        self.assertEqual(game.TIE, game.playRound(game.PAPER, game.PAPER))
    
    def test_paper_vs_rock(self):
        self.assertEqual(game.PLAYER1, game.playRound(game.PAPER, game.ROCK))
    
    def test_paper_vs_scissors(self):
        self.assertEqual(game.PLAYER2, game.playRound(game.PAPER, game.SCISSORS))

    def test_scissors_vs_scissors(self):
        self.assertEqual(game.TIE, game.playRound(game.SCISSORS, game.SCISSORS))

    def test_scissors_vs_paper(self):
        self.assertEqual(game.PLAYER1, game.playRound(game.SCISSORS, game.PAPER))
    
    def test_scissors_vs_rock(self):
        self.assertEqual(game.PLAYER2, game.playRound(game.SCISSORS, game.ROCK))

if __name__ == '__main__':
    unittest.main()