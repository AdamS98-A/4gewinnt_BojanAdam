# 4Gewinnt - Bojan & Adam - Specifications


Our Game consists of 3 Classes: 4Connect, Gameboard and Player.

In "Player" we will display the Participants of the game.
We will save the name, a counter for the last turn and if he's the winner.

In "Gameboard" we will display the Gameboard, which means we save the empty and the filled spots. Here will be a Method for setting a stone. 

In "4Connect" the actual game-session will be displayed and managed.
Methods like Check-Win or Computer_Place_Stone will help to run the game.


- Class Gameboard
   - Method Show_Board
   - Method Place_Stone
   - Attribute Board: Collection
 
- Class 4Connect
   - Method Check_Win
   - Method Print_Winner
   - Method Start_Game -> vl im init?
   - Method Cancel_Game
   - Method Computer_Place_Stone
   - Attribute Player 1: Player
   - Attribute Player 2: Player
   - Attribute Computer: Player
 

- Class Player
   - Attribute Name: string
   - Attribute Turn_Count: int
   - Attribute Winner: boolean


- Changes we needed to make:
   - rename 4connect.py file, file should not start with number
   - needed way more logic for Check_Win Algo.
   - Method Print_Winner wasnt needed
   - 2 Methods for running the Game in seperate Game-Modes were additionaly needed
   - Check for Draw Condition Method was also not defined beforehand