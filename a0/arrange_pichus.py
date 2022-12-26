#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Fall 2022.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    solution= 1
    # Checking all the rows above
    for i in range (row, -1, -1):
        # checking for other p's
        if house_map[i][col]=="p":
            solution =0
            break
        # checking for X 
        elif house_map[i][col]=="X":
            break
    # Checking all the rows below
    for i in range (row, len(house_map)):
        # checking for other p's
        if house_map[i][col] == "p":
            solution=0
            break
        # checking for X
        elif house_map[i][col]=="X":
            break

    # Checking all left up diagonal elements
    k=1
    for i in range(col, -1, -1):
        print 
        if row-k >=0  and house_map[row-k][i-1]=="p": 
            solution=0
            break
        elif row-k >=0 and house_map[row-k][i-1]=="X":
            break
        k=k+1
    # Checking all left down diagonal elements
    k=1
    for i in range(col, -1, -1):
        if row+k <len(house_map)  and house_map[row+k][i-1]=="p":
            solution =0
            break
        elif row+k <len(house_map)  and house_map[row+k][i-1]=="X":
            break
        k=k+1
    # Checking right to left columns 
    for i in range(col, -1, -1):
        # checking for other p's in cols 
        if house_map[row][i]=="p":
            solution=0
            break
        # checking for X
        elif house_map[row][i]=="X":
            break
    # Checking for right up diagonal elements
    k=1
    for i in range(col, len(house_map[0])):
        if row-k >=0  and i+1 <len(house_map[1]) and house_map[row-k][i+1]=="p":
            solution =0
            break
        elif row-k >=0 and i+1 <len(house_map[1])  and house_map[row-k][i+1]=="X":
            break
        k=k+1
    # Checking for right down diagonal elements
    k=1
    for i in range(col, len(house_map[0])):
        if row+k<len(house_map) and i+1 <len(house_map[1]) and house_map[row+k][i+1]=="p": #i+k
            solution=0
            break
        elif row+k<len(house_map) and i+1 <len(house_map[1]) and house_map[row+k][i+1]=="X":
            break
        k=k+1
    # Checking left yo right cols, left to right upward diagonal and right to left downward diagonal
    for i in range(col, len(house_map[0])):
        # checking for other p's in cols
        if house_map[row][i]=="p":
            solution =0
            break
        # cheking for X 
        elif house_map[row][i]=="X":
            break
        k=k+1 

    return (house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]) if solution==1 else []

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = [house_map,k] if k ==1 else solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution else "False")
