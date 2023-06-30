class Position:
    """
    Position class used to represent the physical location of a piece.
    Location is based on the x, y position.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Piece:
    """Piece Superclass. All piece objects inherit the Piece class"""

    def __init__(self, position, color):
        self.posn = position
        self.color = color

    def move(self, posn_2):
        """Abstract base class for moving."""
        print("Invalid move.")

class Pawn(Piece):
    shape = "P"
    type = "Pawn"
    value = 2

    def move(self, posn_2):
        """Move pawn 1 space forward, unless on the first move of *this* pawn, then 2 spaces are allowed"""

        x_diff = abs(ord(posn_2.x) - ord(self.posn.x))
        y_diff = abs(int(posn_2.y) - int(self.posn.y))

        # Check if capturing opponent's piece diagonally
        if (
            (x_diff == 1 and y_diff == 1 and self.color == "white" and self.posn.y != "7") or
            (x_diff == 1 and y_diff == 1 and self.color == "black" and self.posn.y != "2")
        ):
            self.posn = posn_2
            return True

        # Check regular pawn movement
        if (
            (x_diff == 0 and y_diff == 1 and self.color == "white") or
            (x_diff == 0 and y_diff == -1 and self.color == "black") or
            (x_diff == 0 and y_diff == 2 and self.color == "white" and self.posn.y == "2") or
            (x_diff == 0 and y_diff == -2 and self.color == "black" and self.posn.y == "7")
        ):
            self.posn = posn_2
            return True

        return False




class Knight(Piece):
    shape = "G"
    type = "Knight"
    value = 3

    def move(self, posn_2):
        """Move Knight in L shape in any direction"""
        x_diff = abs(ord(posn_2.x) - ord(self.posn.x))
        y_diff = abs(int(posn_2.y) - int(self.posn.y))

        if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
            self.posn = posn_2
            return True

        return False


class Rook(Piece):
    shape = "R"
    type = "Rook"
    value = 7

    def move(self, posn_2):
        """Move Rook * spaces on vertical or horizontal path"""
        if (posn_2.y == self.posn.y or posn_2.x == self.posn.x) and (posn_2.y != self.posn.y or posn_2.x != self.posn.x):
            self.posn = posn_2
            return True
        return False


class Bishop(Piece):
    shape = "B"
    type = "Bishop"
    value = 7

    def move(self, posn_2):
        """Move bishop * spaces on diagonal path"""
        y_diff = abs(int(posn_2.y) - int(self.posn.y))
        x_diff = abs(ord(posn_2.x) - ord(self.posn.x))
        if y_diff == x_diff:
            self.posn = posn_2
            return True
        return False


class Queen(Piece):
    shape = "Q"
    type = "Queen"
    value = 7

    def move(self, posn_2):
        """Move Queen * spaces in any direction"""
        if Bishop.move(self, posn_2) or Rook.move(self, posn_2):
            self.posn = posn_2
            return True
        return False


class King(Piece):
    shape = "K"
    type = "King"
    value = 1

    def move(self, posn_2):
        """Move King 1 space in any direction"""
        if abs(int(posn_2.y) - int(self.posn.y)) <= self.value and abs(ord(posn_2.x) - ord(self.posn.x)) <= self.value:
            self.posn = posn_2
            return True
        return False
