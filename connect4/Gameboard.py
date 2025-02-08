

import Player

class Gameboard:
    #ChatGPT
    # ANSI Escape-Codes for Colors
    __RED = '\033[31m'    # Rot
    __GREEN = '\033[32m'  # Grün
    __RESET = '\033[0m'   # Zurücksetzen auf Standardfarbe
    # Output with different Colors
    # print(f"{GREEN}O{RESET} {RED}o{RESET}")

    def __init__(self, player1: Player, player2: Player):
        self.Collection = [['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],]
        self.player1 = player1
        self.player2 = player2
        
        


    def __repr__(self):
        return f'{self.Collection}'
    
    # Here the Gameboard will be printed
    # it will show the current score
    def Show_Board(self):
        string_4_print = ""
        for row in self.Collection:
            for column in row:
                string_4_print += column + "   "
            print(string_4_print)
            string_4_print = ""


    # Here a Stone is thrown into a column
    # the return value describes, if the Stone placing was successfull or not
    # it wont be successfull, if the column is already full
    # print(f"{GREEN}O{RESET} {RED}o{RESET}")
    def Place_Stone(self, column: int, player: Player) -> bool:
        column = column-1
        if self.Collection[0][column] == "o":
            return False
        
        for i in range(5, -1, -1):
            if self.Collection[i][column] == "x":
                if player == self.player1:
                    self.Collection[i][column] = f'{self.__GREEN}o{self.__RESET}'
                elif player == self.player2:
                    self.Collection[i][column] = f'{self.__RED}o{self.__RESET}'
                return True
        
            


    
    def increase_Turn_Counter(self):
        self.current_turn += 1


if __name__ == '__main__':
    player1 = Player.Player("Bojan",0,False)
    player2 = Player.Player("Adam",0,False)
    s = Gameboard(player1,player2)
    s.Show_Board()

    s.Place_Stone(1,player1)
    s.Place_Stone(1,player1)
    s.Place_Stone(1,player2)

    s.Place_Stone(2,player1)
    s.Place_Stone(2,player2)

    s.Place_Stone(3,player2)

    s.Place_Stone(7,player1)

    print("------------------------------------------------")
    s.Show_Board()

