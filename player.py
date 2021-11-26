

class Player:

    def __init__(self, simbol,name):
        self.simbol = simbol
        self.position_list = [0,0,0,0,0,0,0,0,0,0]
        self.name = name

    def restart_player(self):
        self.position_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


