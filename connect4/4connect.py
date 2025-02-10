import Gameboard
import Player
import random
import time



def start_Game() -> str:


    gamemode=""

    print("-- Hello Player!                                                  --")
    print("-- We welcome you to our 4Connect Game, made by Bojan and Adam!   --")
    print("-- select X at any Input, if you want to end the game             --")

    print("-- Please select which Game-Mode you want to play:                --")
    print("-- Co-Op = A                                                      --")
    print("-- PC = B                                                         --")
    

    while True:
        gamemode = input("-- Game-Mode:")
        if gamemode == "A" or gamemode == "B" or gamemode == "X":
            break
        else:
            print("-- You need to select A or B!                                     --")
            print("-- select X if you want to end the game                           --")

    return gamemode

def Check_Win(gameb: Gameboard, column: int, playerX: Player) -> bool:
    column = (int(column)-1)
    row = findRowWithO(gameb, column)
    win = False
    counter = 0

    #\033[32mo\033[0m Grün
    # \033[31mo\033[0m Rot
    # horizontal
    # letzter Stein = gameb.Gameboard[row][column]
    # h. rechts
    # muss nicht nach links und rechts schauen! entweder 3 nach links oder 3 nach rechts, oder 2 nach links 2 nach rechts
    


    if playerX == gameb.player1:
        # horizontal
        # 1,1,1,x - 1,1,x,1 - 1,x,1,1 - x,1,1,1
        if column >= 3:
            if gameb.Collection[row][column-1] == "\033[32mo\033[0m" and gameb.Collection[row][column-2] == "\033[32mo\033[0m" and gameb.Collection[row][column-3] == "\033[32mo\033[0m":
                return True
        if column <= 3:  
            if gameb.Collection[row][column+1] == "\033[32mo\033[0m" and gameb.Collection[row][column+2] == "\033[32mo\033[0m" and gameb.Collection[row][column+3] == "\033[32mo\033[0m":
                return True
        if column >= 1 and column <= 4:
            if gameb.Collection[row][column-1] == "\033[32mo\033[0m" and gameb.Collection[row][column+1] == "\033[32mo\033[0m" and gameb.Collection[row][column+2] == "\033[32mo\033[0m": 
                return True
        if column <= 5 and column >= 2:
            if gameb.Collection[row][column+1] == "\033[32mo\033[0m" and gameb.Collection[row][column-1] == "\033[32mo\033[0m" and gameb.Collection[row][column-2] == "\033[32mo\033[0m":
                return True
        
        # vertical
        # x ; 1 ; 1 ; 1
        # 1 ; x ; 1 ; 1
        # 1 ; 1 ; x ; 1
        # 1 ; 1 ; 1 ; x
        # actually a bit unnecessary -> only Scenario 1 is important, because Stones can only be placed at the Top of a Queue
        # no time for change
        if row <= 2:
            if gameb.Collection[row+1][column] == "\033[32mo\033[0m" and gameb.Collection[row+2][column] == "\033[32mo\033[0m" and gameb.Collection[row+3][column] == "\033[32mo\033[0m":
                return True 
        if row >= 3:
            if gameb.Collection[row-1][column] == "\033[32mo\033[0m" and gameb.Collection[row-2][column] == "\033[32mo\033[0m" and gameb.Collection[row-3][column] == "\033[32mo\033[0m":
                return True 
        if row >= 1 and row <=3:
            if gameb.Collection[row-1][column] == "\033[32mo\033[0m" and gameb.Collection[row+1][column] == "\033[32mo\033[0m" and gameb.Collection[row+2][column] == "\033[32mo\033[0m":
                return True 
        if row <= 4 and row >= 2:
            if gameb.Collection[row+1][column] == "\033[32mo\033[0m" and gameb.Collection[row-1][column] == "\033[32mo\033[0m" and gameb.Collection[row-2][column] == "\033[32mo\033[0m":
                return True 
            
        # diagonal
        # 1 ; 0 ; 0 ; 0 - 
        # 0 ; x ; 0 ; 0
        # 0 ; 0 ; 1 ; 0
        # 0 ; 0 ; 0 ; 1

        # diagonale links unten -> rechts oben
        if row <= 2 and column >= 3:  # Überprüfen, ob genug Platz nach unten links ist
            if gameb.Collection[row+1][column-1] == "\033[32mo\033[0m" and gameb.Collection[row+2][column-2] == "\033[32mo\033[0m" and gameb.Collection[row+3][column-3] == "\033[32mo\033[0m":
                return True

        # diagonale links oben -> rechts unten
        if row >= 3 and column >= 3:  # Überprüfen, ob genug Platz nach oben links ist
            if gameb.Collection[row-1][column-1] == "\033[32mo\033[0m" and gameb.Collection[row-2][column-2] == "\033[32mo\033[0m" and gameb.Collection[row-3][column-3] == "\033[32mo\033[0m":
                return True
    
        # diagonale links unten -> rechts oben (mittlere Fälle)
        if row <= 2 and column <= 3:  # Überprüfen, ob genug Platz nach unten links und oben rechts ist
            if gameb.Collection[row+1][column+1] == "\033[32mo\033[0m" and gameb.Collection[row+2][column+2] == "\033[32mo\033[0m" and gameb.Collection[row+3][column+3] == "\033[32mo\033[0m":
                return True
        
        # diagonale rechts unten -> links oben
        if row >= 3 and column <= 3:  # Überprüfen, ob genug Platz nach oben rechts ist
            if gameb.Collection[row-1][column+1] == "\033[32mo\033[0m" and gameb.Collection[row-2][column+2] == "\033[32mo\033[0m" and gameb.Collection[row-3][column+3] == "\033[32mo\033[0m":
                return True

    
    elif playerX == gameb.player2:
        # horizontal
        # 1,1,1,x - 1,1,x,1 - 1,x,1,1 - x,1,1,1
        if column >= 3:
            if gameb.Collection[row][column-1] == "\033[31mo\033[0m" and gameb.Collection[row][column-2] == "\033[31mo\033[0m" and gameb.Collection[row][column-3] == "\033[31mo\033[0m":
                return True
        if column <= 3:  
            if gameb.Collection[row][column+1] == "\033[31mo\033[0m" and gameb.Collection[row][column+2] == "\033[31mo\033[0m" and gameb.Collection[row][column+3] == "\033[31mo\033[0m":
                return True
        if column >= 1 and column <= 4:
            if gameb.Collection[row][column-1] == "\033[31mo\033[0m" and gameb.Collection[row][column+1] == "\033[31mo\033[0m" and gameb.Collection[row][column+2] == "\033[31mo\033[0m": 
                return True
        if column <= 5 and column >= 2:
            if gameb.Collection[row][column+1] == "\033[31mo\033[0m" and gameb.Collection[row][column-1] == "\033[31mo\033[0m" and gameb.Collection[row][column-2] == "\033[31mo\033[0m":
                return True
        
        # vertical
        # x ; 1 ; 1 ; 1
        # 1 ; x ; 1 ; 1
        # 1 ; 1 ; x ; 1
        # 1 ; 1 ; 1 ; x
        # actually a bit unnecessary -> only Scenario 1 is important, because Stones can only be placed at the Top of a Queue
        # no time for change
        if row <= 2:
            if gameb.Collection[row+1][column] == "\033[31mo\033[0m" and gameb.Collection[row+2][column] == "\033[31mo\033[0m" and gameb.Collection[row+3][column] == "\033[31mo\033[0m":
                return True 
        if row >= 3:
            if gameb.Collection[row-1][column] == "\033[31mo\033[0m" and gameb.Collection[row-2][column] == "\033[31mo\033[0m" and gameb.Collection[row-3][column] == "\033[31mo\033[0m":
                return True 
        if row >= 1 and row <=3:
            if gameb.Collection[row-1][column] == "\033[31mo\033[0m" and gameb.Collection[row+1][column] == "\033[31mo\033[0m" and gameb.Collection[row+2][column] == "\033[31mo\033[0m":
                return True 
        if row <= 4 and row >= 2:
            if gameb.Collection[row+1][column] == "\033[31mo\033[0m" and gameb.Collection[row-1][column] == "\033[31mo\033[0m" and gameb.Collection[row-2][column] == "\033[31mo\033[0m":
                return True 
            

        # diagonal
        # 1 ; 0 ; 0 ; 0 
        # 0 ; x ; 0 ; 0
        # 0 ; 0 ; 1 ; 0
        # 0 ; 0 ; 0 ; 1
            
        # diagonale links unten -> rechts oben
        if row <= 2 and column >= 3:  # Überprüfen, ob genug Platz nach unten links ist
            if gameb.Collection[row+1][column-1] == "\033[31mo\033[0m" and gameb.Collection[row+2][column-2] == "\033[31mo\033[0m" and gameb.Collection[row+3][column-3] == "\033[31mo\033[0m":
                return True

        # diagonale links oben -> rechts unten
        if row >= 3 and column >= 3:  # Überprüfen, ob genug Platz nach oben links ist
            if gameb.Collection[row-1][column-1] == "\033[31mo\033[0m" and gameb.Collection[row-2][column-2] == "\033[31mo\033[0m" and gameb.Collection[row-3][column-3] == "\033[31mo\033[0m":
                return True
        
        # diagonale links unten -> rechts oben (mittlere Fälle)
        if row <= 2 and column <= 3:  # Überprüfen, ob genug Platz nach unten links und oben rechts ist
            if gameb.Collection[row+1][column+1] == "\033[31mo\033[0m" and gameb.Collection[row+2][column+2] == "\033[31mo\033[0m" and gameb.Collection[row+3][column+3] == "\033[31mo\033[0m":
                return True
        
        # diagonale rechts unten -> links oben
        if row >= 3 and column <= 3:  # Überprüfen, ob genug Platz nach oben rechts ist
            if gameb.Collection[row-1][column+1] == "\033[31mo\033[0m" and gameb.Collection[row-2][column+2] == "\033[31mo\033[0m" and gameb.Collection[row-3][column+3] == "\033[31mo\033[0m":
                return True

   
    return False

def Check_Draw(gameb: Gameboard) -> bool:
    return False

def findRowWithO(gameb: Gameboard, column: int) -> int:
    for i in range(0, 6): #5, -1, -1
        if gameb.Collection[i][column] != "x":
            return i

    return 5
    


def run_CO_OP_Mode():
    print("-- Co-OP Mode is activated                                        --")
    player1_name = input("-- Please enter the Name of Player 1: ")
    if player1_name == "X": StopGame() 
    player2_name = input("-- Please enter the Name of Player2: ")
    if player2_name == "X": StopGame()
    player1 = Player.Player(player1_name,0,False)
    player2 = Player.Player(player2_name,0,False)
    gameb = Gameboard.Gameboard(player1,player2)

    print("-- !Let's Start!                                                  --")
    gameb.Show_Board()

    while True:
        column = input(f'-- {player1.name}, please select a column-number: ')
        if column == "X": StopGame() 
        gameb.Place_Stone(int(column), player1)
        player1.increase_Turn_Counter()
        gameb.Show_Board()
        if player1.current_turn >= 4 and Check_Win(gameb, column, player1) == True:
            print("------ WINNER WINNER CHICKEN DINNER           ------")
            print(f"------ {player1.name.upper()} IS THE WINNER                  ------")
            break

        column = input(f'-- {player2.name}, please select a column: ')
        if column == "X": StopGame() 
        gameb.Place_Stone(int(column), player2)
        player2.increase_Turn_Counter()
        gameb.Show_Board()
        if player2.current_turn >= 4 and Check_Win(gameb, column, player2) == True:
            print("------ WINNER WINNER CHICKEN DINNER           ------")
            print(f"------ {player2.name.upper()} IS THE WINNER                  ------")
            break


    print("")

def run_PC_Mode():
    print("-- Co-OP Mode is activated                                        --")
    player_name = input("-- Please enter your Name: ")
    if player_name == "X": StopGame()
    player1 = Player.Player(player_name,0,False)
    playerPC = Player.Player("PC",0,False)
    gameb = Gameboard.Gameboard(player1,playerPC)

    print("-- !Let's Start!                                                  --")
    gameb.Show_Board()
    
    while True:
        column = input(f'{player1.name}, please select a column-number: ')
        if column == "X": StopGame() 
        gameb.Place_Stone(int(column), player1)
        player1.increase_Turn_Counter()
        gameb.Show_Board()

        if player1.current_turn >= 4 and Check_Win(gameb, column, player1) == True:
            print("------ WINNER WINNER CHICKEN DINNER                   ------")
            print(f"------ {player1.name.upper()} IS THE WINNER                  ------")
            break

        boolPlaceStone = True
        counterPlaceStone = 0
        print(f'{playerPC.name}, please select a column-number: ')
        time.sleep(1)

        while boolPlaceStone:
            random_column = random.randint(1, 7)
            counterPlaceStone += 1
            if gameb.Place_Stone(int(random_column), playerPC):
                print(f'{playerPC.name}, please select a column-number: {random_column}')
                boolPlaceStone = False
            elif counterPlaceStone > 20:
                break
            
        if boolPlaceStone:
            print("Es konnte leider keine freie Spalte gefunden werden!")
            exit()
        
        if playerPC.current_turn >= 4 and Check_Win(gameb, column, playerPC) == True:
            print("------ WINNER WINNER CHICKEN DINNER                   ------")
            print(f"------ {playerPC.name.upper()} IS THE WINNER                  ------")
            break
            
        playerPC.increase_Turn_Counter()
        gameb.Show_Board()


    print("")


def StopGame():
    print("-- Game Over! Thank You!                                          --")
    exit()
    



if __name__ == '__main__':
    gamemode = start_Game()

    if gamemode == "A":
        run_CO_OP_Mode()
    elif gamemode=="B":
        run_PC_Mode()
    else:
        print("-- Game Over! Thank You!                                          --")





