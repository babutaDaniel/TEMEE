from board import Board
from player import Player

class Game:

    def start_game(self):

        player1 = Player("X", "Player1")
        player2 = Player("O", "Player2")

        Board().display_board()
        player = player1
        board = Board()
        game_still_going = True

        while game_still_going is True:
            position = board.handle_turn(player, board)
            board.update_cell(position, player.simbol)
            board.display_board()

            if self.check_if_game_over(player, board) is True:
                game_still_going = False

            player = self.flip_player(player, player1, player2)

        print("Do you want to play again? (Press y for YES, Press n for No")
        restart = input("Your choice :")

        if restart == 'y':
            player1.position_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            player2.position_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            Board.board = ["0",
                            "1", "2", "3",
                            "4", "5", "6",
                            "7", "8", "9", ]

            Game().start_game()
        else:
            print("Game ended.")



    def check_if_game_over(self, player,board):

        if board.if_win(player,board) is True:
            print(f"{player.name} won the game. Have another game?")
            return True

        if board.if_draw(board) is True:
            print("Game ended as a draw. Have another game?")
            return True


    def flip_player(self, player,player1,player2):
        if player.name == player1.name:
            player = player2
        else:
            player = player1
        return player

    def restart(self):
        print("(Press y for YES, Press n for No)")
        restart = input("Your choice :")

