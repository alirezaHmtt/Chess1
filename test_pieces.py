import unittest
from pieces import *

class TestChessPieces(unittest.TestCase):
    def test_pawn_move(self):
        pawn = Pawn(Position('E', '2'), 'white')

        # Test valid moves
        self.assertTrue(pawn.move(Position('E', '3')))
        self.assertTrue(pawn.move(Position('E', '4')))

        # Test invalid moves
        self.assertFalse(pawn.move(Position('D', '3')))  # Diagonal move without capturing
        self.assertFalse(pawn.move(Position('E', '5')))  # Move more than 2 spaces

    def test_knight_move(self):
        knight = Knight(Position('B', '1'), 'white')

        # Test valid moves
        self.assertTrue(knight.move(Position('C', '3')))
        self.assertTrue(knight.move(Position('A', '3')))

        # Test invalid moves
        self.assertFalse(knight.move(Position('C', '4')))  # Not an L-shape move
        self.assertFalse(knight.move(Position('D', '2')))  # Not an L-shape move

    def test_rook_move(self):
        rook = Rook(Position('A', '1'), 'white')

        # Test valid moves
        self.assertTrue(rook.move(Position('A', '5')))
        self.assertTrue(rook.move(Position('H', '1')))

        # Test invalid moves
        self.assertFalse(rook.move(Position('B', '2')))  # Diagonal move
        self.assertFalse(rook.move(Position('H', '2')))  # L-shape move

    def test_bishop_move(self):
        bishop = Bishop(Position('C', '1'), 'white')

        # Test valid moves
        self.assertTrue(bishop.move(Position('F', '4')))
        self.assertTrue(bishop.move(Position('A', '7')))

        # Test invalid moves
        self.assertFalse(bishop.move(Position('D', '2')))  # Not a diagonal move
        self.assertFalse(bishop.move(Position('E', '5')))  # Not a diagonal move

    def test_queen_move(self):
        queen = Queen(Position('D', '1'), 'white')

        # Test valid moves
        self.assertTrue(queen.move(Position('D', '4')))
        self.assertTrue(queen.move(Position('H', '1')))

        # Test invalid moves
        self.assertFalse(queen.move(Position('E', '3')))  # Not a valid move for queen
        self.assertFalse(queen.move(Position('G', '5')))  # Not a valid move for queen

    def test_king_move(self):
        king = King(Position('E', '1'), 'white')

        # Test valid moves
        self.assertTrue(king.move(Position('E', '2')))
        self.assertTrue(king.move(Position('F', '1')))

        # Test invalid moves
        self.assertFalse(king.move(Position('E', '4')))  # Move more than 1 space
        self.assertFalse(king.move(Position('G', '1')))  # Move more than 1 space

if __name__ == '__main__':
    unittest.main()
