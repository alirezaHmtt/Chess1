from termcolor import colored


class Piece:
    def __init__(self, shape, color, posn):
        self.shape = shape
        self.color = color
        self.posn = posn


class Board:
    def __init__(self):
        self.board = self.initialize()
        self.king_pos = {"white": (7, 4), "black": (0, 4)}

    def initialize(self):
        """Initialize the game board"""
        board = [["X" for _ in range(8)] for _ in range(8)]

        for i in range(8):
            board[1][i] = "P"
            board[6][i] = "P"

        for i in range(0, 8, 7):
            board[i][0] = "R"
            board[i][1] = "G"
            board[i][2] = "B"
            board[i][3] = "Q"
            board[i][4] = "K"
            board[i][5] = "B"
            board[i][6] = "G"
            board[i][7] = "R"
        return board

    def print_board(self):
        numbers = '87654321'
        print()
        for i in range(8):
            print(numbers[i], end="  ")
            for k in range(8):
                print(self.board[i][k], end=" ")
            print()
        print()
        print("   A B C D E F G H")

    @staticmethod
    def convert_letter_to_num(posn):
        """Converts a posn.x value from letter to number for indexing in the board array"""
        letters = 'ABCDEFGH'
        i = 0
        for letter in letters:
            if posn.x == letter:
                return i
            i += 1

    def can_capture(self, attacker_pos, target_pos):
        attacker = self.board[attacker_pos[0]][attacker_pos[1]]
        if attacker == "P":
            if attacker_pos[0] - 1 == target_pos[0] and abs(attacker_pos[1] - target_pos[1]) == 1:
                return True
        elif attacker == "R":
            if attacker_pos[0] == target_pos[0] or attacker_pos[1] == target_pos[1]:
                if self.is_path_clear(attacker_pos, target_pos):
                    return True
        elif attacker == "G":
            offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
            for offset in offsets:
                new_pos = (attacker_pos[0] + offset[0], attacker_pos[1] + offset[1])
                if new_pos == target_pos:
                    return True
        elif attacker == "B":
            if abs(attacker_pos[0] - target_pos[0]) == abs(attacker_pos[1] - target_pos[1]):
                if self.is_path_clear(attacker_pos, target_pos):
                    return True
        elif attacker == "Q":
            if (
                attacker_pos[0] == target_pos[0]
                or attacker_pos[1] == target_pos[1]
                or abs(attacker_pos[0] - target_pos[0]) == abs(attacker_pos[1] - target_pos[1])
            ):
                if self.is_path_clear(attacker_pos, target_pos):
                    return True
        elif attacker == "K":
            offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for offset in offsets:
                new_pos = (attacker_pos[0] + offset[0], attacker_pos[1] + offset[1])
                if new_pos == target_pos:
                    return True
        return False




    def is_check(self, color):
        king_pos = self.king_pos[color]

        # Check if any opponent's piece can capture the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != "X" and piece.islower() and piece != color:
                    posn = (row, col)
                    if self.can_capture(posn, king_pos):
                        return True

        return False


    def is_checkmate(self, color):
        king_pos = self.king_pos[color]

        # Check if any opponent's piece can capture the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece != "X" and piece.islower() and piece != color:
                    posn = (row, col)
                    if self.can_capture(posn, king_pos):
                        return True
        return False


    def is_path_clear(self, from_posn, to_posn):
        if from_posn[0] == to_posn[0]:
            start_col = min(from_posn[1], to_posn[1]) + 1
            end_col = max(from_posn[1], to_posn[1])
            for col in range(start_col, end_col):
                if self.board[from_posn[0]][col] != "X":
                    return False
        elif from_posn[1] == to_posn[1]:
            start_row = min(from_posn[0], to_posn[0]) + 1
            end_row = max(from_posn[0], to_posn[0])
            for row in range(start_row, end_row):
                if self.board[row][from_posn[1]] != "X":
                    return False
        else:
            start_row = min(from_posn[0], to_posn[0]) + 1
            end_row = max(from_posn[0], to_posn[0])
            start_col = min(from_posn[1], to_posn[1]) + 1
            end_col = max(from_posn[1], to_posn[1])
            row = start_row
            col = start_col
            while row < end_row and col < end_col:
                if self.board[row][col] != "X":
                    return False
                row += 1
                col += 1
        return True





    def update_board(self, from_posn, piece):
        old_x_value = self.convert_letter_to_num(from_posn)
        new_x_value = self.convert_letter_to_num(piece.posn)

        is_capture, value = self.capture_piece(piece, new_x_value)
        if is_capture:
            print(
                colored("Your {0} captured the Bot's {1}!".format(piece.type, self.convert_value_to_type(value)), "green")
            )

        # Update king position if the moved piece is a king
        if piece.shape == "K":
            self.king_pos[piece.color] = (8 - int(piece.posn.y), new_x_value)
            self.board[8 - int(from_posn.y)][old_x_value] = "X"
            self.board[8 - int(piece.posn.y)][new_x_value] = piece.shape

        if self.is_check(piece.color):
            print(colored("Check!", "red"))
        if self.is_checkmate(piece.color):
            print(colored("Checkmate!", "red"))


    def capture_piece(self, piece, x_posn):
        value = self.board[8 - int(piece.posn.y)][x_posn]
        if value != "X":
            if value == "K":
                print(colored("Check!", "red"))
                if self.is_checkmate(piece.color):
                    print(colored("Checkmate!", "red"))
            return True, value
        return False, value

    @staticmethod
    def convert_value_to_type(value):
        if value == "P":
            return "Pawn"
        if value == "R":
            return "Rook"
        if value == "G":
            return "Knight"
        if value == "B":
            return "Bishop"
        if value == "Q":
            return "Queen"
        if value == "K":
            return "King"

