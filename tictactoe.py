"""
tictactoe.py
Store a 3 by 3 tic-tac-toe board in a list of 3 lists and see who won
"""

import sys

b = [
    ["X", "X", " "],
    ["X", "O", "O"],
    ["X", " ", "O"]
]

lines = [   #lines is a list of 8 strings.
    #3 rows
    b[0],   #top row
    b[1],  #middle row
    b[2],

    #3 columns
    [b[0][0],b[1][0],b[2][0]],  #left column
    [b[0][1],b[1][1],b[2][1]], #middle column
    [b[0][2],b[1][2],b[2][2]], #right column,,

    #2 diagonals
    [b[0][2],b[1][1],b[2][0]],  #upper left to lower right
    [b[0][0],b[1][1],b[2][2]] #upper right to lower left
]

for strikes in lines:
    if strikes == ["O", "O", "O"]:
        print("O won")
    if strikes == ["X", "X", "X"]:
        print("X won")
