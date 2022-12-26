#!/usr/local/bin/python3
# solver2022.py : 2022 Sliding tile puzzle solver
#
# Code by: lharwin-aniiyer-a1 (Laya Harwin and Anirudh Iyer)
#
# Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
#

import sys
import numpy as np
from queue import PriorityQueue
import copy
ROWS=5
COLS=5

# return a list of possible successor states
def Find_Successors(s):
    succ_output=[*Rotate_Row(s),*Rotate_Col(s)]
    succ_output.append(Rotate_OuterClockwise(copy.deepcopy(s)))
    succ_output.append(Rotate_OuterCounterClockwise(copy.deepcopy(s)))
    succ_output.append(Rotate_InnerClockwise(copy.deepcopy(s)))
    succ_output.append(Rotate_InnerCounterClockwise(copy.deepcopy(s)))
    return succ_output

# Function to update the heuristic fucntion
def Heuristic_Function(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            count = count + abs(i - (state[i][j]-1)//ROWS ) + abs(j-(state[i][j]-1)%COLS)
    return count

# check if we've reached the goal
def is_goal(state):
    count = 1
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j]!=count:
                return False
            count += 1
    return True

# Function to generate moves
def  moves_list():
    out=[]
    for i in range(1,6):
        out.append(f'L{i}')
        out.append(f'R{i}')
    for j in range(1,6):
        out.append(f'U{j}')
        out.append(f'D{j}')
    out.append('Oc')
    out.append('Occ')
    out.append('Ic')
    out.append('Icc')
    return out
   # print(out)


def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    state = [[initial_board[j+i] for j in range(5)] for i in range(0,25,5)]
    moves=moves_list()
    Fringe_Priority_Queue = PriorityQueue()
    Fringe_Priority_Queue.put((0,(state, [], "", 0)))

    while not Fringe_Priority_Queue.empty():
        h1, (state, path, move_path, d) = Fringe_Priority_Queue.get(0)
        if is_goal(state):
            return list(move_path.split(" "))[1:]
        temp = 0
        for s in Find_Successors(state):
            Fringe_Priority_Queue.put((d+1+Heuristic_Function(s),(s, path+[state,], move_path + " " + moves[temp], d+1)))
            temp += 1
    return []

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

# Function to rotate row
def Rotate_Row(s):
    output_row = []
    for i in range(0,5):
        x = [i][0]
        j =0 
        temp = copy.deepcopy(s)
        length1= len(s)
        while length1-1>j:
            temp[i][j] = s[i][j+1]
            j= j + 1
        temp[i][4] = x
        output_row.append(temp)
        temp = copy.deepcopy(s)
        y = s[i][-1]
        j=0
        temp = copy.deepcopy(s)
        length2= len(s)
        while length2-1>j:
            temp[i][j+1] = s[i][j]
            j+=1
        temp[i][0] = y
        output_row.append(temp)
    return output_row

# Function to rotate column
def Rotate_Col(s):
    output_col = []
    length = len(s[0])
    for i in range(0, length):
        temp = copy.deepcopy(s)
        x = s[0][i]
        j =1
        length1= len(temp)
        while length1> j :
            temp[j-1][i] = s[j][i]
            j= j +1
        temp[j-1][i] = x
        output_col.append(temp)
        temp = copy.deepcopy(s)
        y = s[4][i]
        j =0
        while len(temp)-1>j:
            temp[j+1][i] = s[j][i]
            j = j + 1
        temp[0][i] = y
        output_col.append(temp)
    return output_col

# Function to rotate outer circle clockwise
def Rotate_OuterClockwise(s):
    k=5
    x = s[0][4]
    s[0] = [s[1][0], *s[0][0:4]]
    y = s[4][4]
    for i in range(k-1,0,-1):
        s[i][4] = s[i-1][4]
    s[1][4] = x
    z = s[4][0]
    s[4] = [*s[4][1:], s[4][4]]
    s[4][3] = y
    for i in range(k-1):
        s[i][0] = s[i+1][0]
    s[3][0] = z
    return s

# Function to rotate outer circle counter clockwise
def Rotate_OuterCounterClockwise(s):
    m = 0
    n = len(s) -1
    x = s[n][n]
    s[n]= [*s[m][1:],s[1][n]] 
    i = 0
    while i < n:
        s[i][n] = s[i+1][n]
        i += 1
    s[n][n] = s[n][n-1]
    y = s[n][0:n-1]
    s[n] = [s[n-1][n-1],*y,s[n][n]]  
    i=4
    while i>1:
        s[i][0] = s[i-1][0]
        i-=1
    s[1][m] = x
    return s

# Function to rotate inner cicle clockwise
def Rotate_InnerClockwise(s):
    i =0
    j = len(s) -1
    x = s[i+ 1][3]
    s[i+1] = [s[i+1][i],s[2][i+1],s[i+1][i+1],s[i+1][2],s[i+1][j]] 
    y = s[j-1][j]
    s[j-1][j-1] = s[2][j-1]
    s[2][j-1] = x
    z = s[j-1][1]
    s[j-1][i+1] = s[j-1][2]
    s[j-1][2] = y
    s[2][i+1] = z
    return s

# Function to rotate inner counter clockwise
def Rotate_InnerCounterClockwise(s):
    i = 0
    j = len(s) -1
    x = s[i+1][i+1]
    s[i+1] = [s[i+1][i],s[i+1][2],s[i+1][3],s[i+2][3],s[i+1][4]] 
    y = s[j-1][i+1]
    s[j-1][i+1] = s[2][i+1]
    s[2][i+1] = x
    z = s[j-1][j-1]
    s[j-1][j-1] = s[j-1][2]
    s[j-1][2] = y
    s[2][j-1] = z
    return s

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))
    
    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]
    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))
    
    # temp_list = [[start_state[j+i] for j in range(5)] for i in range(0,25,5)]

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
