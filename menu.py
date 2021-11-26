from game import Game
from player import Player



class Menu:

    def validate(self):
        print("This is the menu!")
        print("Chose 1 if you want to play \nChose 0 if you don't want to play")
        chose = input("Your chose:")
        ok = 0
        while ok == 0:
            try:
                chose = int(chose)
                if chose == 1:
                    ok = 1
                    print("The game is starting")
                    Game().start_game()

                elif chose == 0:
                    print("Exit game")
                    ok = 1
                else:
                    print(chose, " is not a valid answer")
                    print("Please type 1 or 0")
                    chose = input("Your chose:")
                    continue

            except:
                print(chose, " is not a valid answer")
                print("Please type 1 or 0")
                chose = input("Your chose:")
                continue








