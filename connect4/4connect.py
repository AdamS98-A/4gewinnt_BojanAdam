import Gameboard
import Player

def start_Game() -> str:


    gamemode=""

    print("-- Hello Player!                                                  --")
    print("-- We welcome you to our 4Connect Game, made by Bojan and Adam!   --")

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

def Check_Win(gameb: Gameboard) -> bool:
    return False
    


def run_CO_OP_Mode():
    print("-- Co-OP Mode is activated                                        --")
    player1_name = input("-- Please enter the Name of Player 1: ")
    player2_name = input("-- Please enter the Name of Player2: ")
    player1 = Player.Player(player1_name,0,False)
    player2 = Player.Player(player2_name,0,False)
    gameb = Gameboard.Gameboard(player1,player2)

    print("-- !Let's Start!                                                  --")
    gameb.Show_Board()

    while True:
        column = input(f'-- {player1.name}, please select a column-number: ')
        gameb.Place_Stone(int(column), player1)
        player1.increase_Turn_Counter()
        gameb.Show_Board()
        if player1.current_turn >= 4 and Check_Win(gameb) == True:
            print("------ WINNER WINNER CHICKEN DINNER                   ------")
            print(f"------ {player1.name.upper()} IS THE WINNER                  ------")
            break

        column = input(f'-- {player2.name}, please select a column: ')
        gameb.Place_Stone(int(column), player2)
        player1.increase_Turn_Counter()
        gameb.Show_Board()
        if player2.current_turn >= 4 and Check_Win(gameb) == True:
            print("------ WINNER WINNER CHICKEN DINNER                   ------")
            print(f"------ {player2.name.upper()} IS THE WINNER                  ------")
            break


    print("")

def run_PC_Mode():
    print("-- Co-OP Mode is activated                                        --")
    player_name = input("-- Please enter your Name: ")
    player1 = Player.Player(player_name,0,False)
    playerPC = Player.Player("PC",0,False)
    gameb = Gameboard.Gameboard(player1,playerPC)


    print("")



if __name__ == '__main__':
    gamemode = start_Game()

    if gamemode == "A":
        run_CO_OP_Mode()
    elif gamemode=="B":
        run_PC_Mode()
    else:
        print("-- Game Over! Thank You!                                          --")





