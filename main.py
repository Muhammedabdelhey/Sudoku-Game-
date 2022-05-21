import random

import numpy as np

def valid(bo, num, pos):
    # Check row
    for i in range(9):
        if bo[pos[0]][i] == num and  pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box pos (8,3)=8
    box_x = pos[1] // 3 #3/3=1  #culm
    box_y = pos[0] // 3 #8/3 =2 # ROW

    for i in range(box_y*3, box_y*3 + 3): #start 2*3=6 ,2*3+3=9 range(6,9)[6,7,8]
        for j in range(box_x * 3, box_x*3 + 3): #start 3*1=3, end 3*1+3 =6 Range (3,6)[3,4,5}
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True



def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)) == True:
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0

    return False



def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")



s_bord = np.zeros((9, 9), int)
for i in range(0,5):
    for j in range(0,5):
         x = random.randint(1,9)#8
         row=random.randint(0, 8)#0
         clum=random.randint(0, 8)#1
         if valid(s_bord, x, (row, clum)) and s_bord[row][clum]==0:
            s_bord[row][clum] = x
         else:
            i=i-1

print("Befor Solve")
print_board(s_bord)
solve(s_bord)
print("\n___________________\nAfter Solve")
print_board(s_bord)


def c_score(bo):

    counter = 0
    for i in range(0, 9):
        for j in range(0, 9):
            num = bo[i][j]
            if valid(bo, num, (i, j)):
                counter = counter + 1
    return counter

print("score is",c_score(s_bord))
