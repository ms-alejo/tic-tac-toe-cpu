# Tic Tac Toe Game

## Overview
This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to play against each other or lets one player play against the CPU. The CPU makes random valid moves during its turn.

## Features
- **Game Modes:**
  - Player vs. Player (PVP)
  - Player vs. CPU (PvCPU)

## How to Play
### 1. Clone or Download the Script
Save the provided `main.py` file on your local machine.

### 2. Run the Game
Run the script using Python:
```bash
python tic_tac_toe.py

### 3. Select Game Mode
Choose between two game modes when prompted:
- Press `1` for Player vs. Player mode.
- Press `2` for Player vs. CPU mode.

### 4. Play the Game
- Players take turns placing their mark (`X` or `O`) on the 3x3 board.
- Enter the row and column indices (0-based) when prompted.
- The game ends when one player gets three in a row or the board is full (draw).

## Example Game Output
``` bash
  0 1 2 
  -----
0|     |
1|     |
2|     |
  -----

Choose a game mode:
1. Player vs. Player (PVP)
2. Player vs. CPU (PvCPU)
Enter 1 or 2: 1
Player X's turn.
Please input your move's X coordinate position?: 1
Please input your move's Y coordinate position?: 1

  0 1 2 
  -----
0|     |
1|  X  |
2|     |
  -----
Player O's turn.
...
```

## Requirements
- Python 3.x

## Future Enhancements
- Add more difficulty levels for the CPU.

## Steps
- [x] Make a board
- [x] Render the board
- [x] Get inputs
- [x] Apply inputs to board
- [x] Make sure everything works
- [x] Winner check
- [x] Testing
- [x] Make a cpu that makes random moves
- [ ] Ask for usernames
- [ ] Networked through TCP?
- [ ] League tables, statistics, and databases
- [ ] Make a cpu that makes winning moves
- [ ] Best AI 
- [ ] Make a cpu that makes winning moves and blocks losing ones
