#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code provided in CSCI B551, Fall 2022.

import sys

# To find which move (L, R, U or D) agent took and append it with the existing path and return it. 
def move_agent (curr_move,move,path):
    #When agent takes a R (RIGHT) move, coloumn index changes. i.e. curr location + 1 = new location
    if curr_move[1] + 1 == move[1]:
        path=''.join((path,'R'))
    #When agent takes a D (DOWN) move, row index changes. i.e. curr location + 1 = new location
    elif curr_move[0] + 1 == move[0]:
        path=''.join((path,'D')) 
    #When agent takes a U (UP) move, row index changes. i.e. curr location - 1 = new location
    elif curr_move[0] -1 == move[0]:
        path=''.join((path,'U'))
    #When agent takes a L (LEFT) move, column index changes. i.e. curr location + 1 = new location
    elif curr_move[1] -1 == move[1]:
        path=''.join((path,'L'))
    return path

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
            return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        #Adding the first node to FRINGE list, i.e start node, which in our case is pichu's location. Along with pichu's location, we are also adding the distance traversed from the start node and the path travelled in terms of U, L, R, and D characters. 
        #The distance travlled and path taken will be 0 and '' respectively because pichu is in its starting position
        fringe=[(pichu_loc,0,'')] 
        #To keep tarck of the nodes visited, adding a list
        visited =[]
        #To keep track of path, consisting of U, L, R, and D characters, adding a string variable
        move_string = ""
        while fringe:
                (curr_move, curr_dist, curr_path)=fringe.pop()
                move_string = curr_path
                visited.append(curr_move)

                for move in moves(house_map, *curr_move):
                        if house_map[move[0]][move[1]]=="@":
                            #Destination node is found. Returing the total distance travelled and total path (in terms of  U, L, R, and D characters) from start node (p) to destination node (@)
                            return (curr_dist + 1, move_agent(curr_move, move, move_string))
                        elif move not in visited:
                            #If destination is not found and the node is not in VISITED list, then we add the move node to FRINGE list.
                            fringe.append((move, curr_dist + 1,move_agent(curr_move, move, move_string)))
# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print((str(solution[0]) + " " + solution[1]) if solution else ("No Path exists!!"))
