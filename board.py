from player import Player

class Board:

    def __init__(self):
        self.board = ["0",
                      "1", "2", "3",
                      "4", "5", "6",
                      "7", "8", "9", ]


    def display_board(self):

        print(self.board[1] + " | " + self.board[2] + " | " + self.board[3])
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6])
        print(self.board[7] + " | " + self.board[8] + " | " + self.board[9])

    def handle_turn(self, player, board):
        position = input("Chose a position from 1-9:")
        while self.validate(position) is False:

            print("Try again")
            position = input("Chose a position from 1-9:")

        position = int(position)
        return position


    def validate(self, position):
        try:
            position = int(position)
        except:
            return False

        if type(position) is int and position <= 9 and position >= 1 and self.board[position] == str(position):
            return True
        else:
            return False

    def update_cell(self, cell_no, player):
        self.board[cell_no] = player

    def if_win(self,player,board):
        win_lines = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]]
        for a, b, c in win_lines:
            if board.board[a] == board.board[b] == board.board[c] == player.simbol:
                return True
        return False

    def if_draw(self, board):
        ok = 0
        for a in range(1, 10):
            if board.board[a] == str(a):
                ok = 1

        if ok == 0:

            return True
        else:

            return False

    def restart_board(self):
        self.board = ["0",
                      "1", "2", "3",
                      "4", "5", "6",
                      "7", "8", "9", ]




