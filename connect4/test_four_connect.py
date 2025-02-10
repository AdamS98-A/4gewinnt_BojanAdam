import unittest
from Gameboard import Gameboard
from Player import Player
from four_connect import Check_Win

class TestFourConnect(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Alice", 0, False)
        self.player2 = Player("Bob", 0, False)
        self.board = Gameboard(self.player1, self.player2)

    def test_valid_move(self):
        """ Tests if a valid move is successfully placed. """
        result = self.board.Place_Stone(1, self.player1)
        self.assertTrue(result)
        self.assertNotEqual(self.board.Collection[5][0], 'x')

    def test_invalid_move_column_full(self):
        """ Tests if placing a stone in a full column is prevented. """
        for _ in range(6):
            self.board.Place_Stone(1, self.player1)
        result = self.board.Place_Stone(1, self.player2)
        self.assertFalse(result)

    def test_win_horizontal(self):
        """ Tests a horizontal win condition. """
        for i in range(4):
            self.board.Place_Stone(i+1, self.player1)
        self.assertTrue(Check_Win(self.board, 4, self.player1))
    
    def test_win_vertical(self):
        """ Tests a vertical win condition. """
        for _ in range(4):
            self.board.Place_Stone(1, self.player1)
        self.assertTrue(Check_Win(self.board, 1, self.player1))
    
    def test_no_win(self):
        """ Tests if a situation without a win is correctly detected. """
        self.board.Place_Stone(1, self.player1)
        self.board.Place_Stone(2, self.player2)
        self.board.Place_Stone(3, self.player1)
        self.board.Place_Stone(4, self.player2)
        self.assertFalse(Check_Win(self.board, 4, self.player2))

if __name__ == "__main__":
    unittest.main()
