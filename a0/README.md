# Assignment 0 - lharwin@iu.edu 

## Introduction
Here, we are attempting to address two problems. 
1. route pichu.py: Pichu must be guided from the source node to the destination node along the shortest path possible while avoiding any obstacles ("X")
2. arrange pichus.py: Set up k Pichus so that none of them can see the others.

## Brief Overview of the solution
### Part 1: route_pichu.py
- To overcome this problem, I applied the idea of a breadth-first search method.
- Changes are made in mainly 2 functions in route_pichu.py.  
a. search and 
b. move_agent


**Changes made in route_pichu: search function**
- To keep track of the nodes visited, added a node called **visited** to the search function. 
- Every time a node is added to fringe, move_string is also added along with pichu_loc and cost. This helps in getting the direction taken to reach that particular node.
- When destination "@" is reached, return the distance traveled and the distance traveled in terms of U, L, R, and D characters
- if the destination is not reached, check if the node is visited or not, if not then we add the node to the fridge


**Changes made in route_pichu: move_agent function**
- move_agent is a new function added to find which move the agent took in terms of U, L, R, and D characters and later append it with the existing path and return it.
- Here, we are checking the row and col index of the current position and previous position and determine if the agent took a top, down, right, or left move.


### Part 2: arrange_pichu.py 
- Here to find the optimal position for kth Pichu, for which its row, columns, and diagonals are checked. 
- This functionality is implemented in add_pichu function. 


**Changes made in arrange_pichu: add_pichu function**
- A toal of 8 loops are implemented for iterating through all positions that can cause conflict with the current Pichu location. 
- 2 loops are used for row iteration, 2 for column iteration and 4 for diagonal iteration. 



## Design Decisions
### Part 1: route_pichu.py: move_agent function
- When the agent takes a right move(R), the coordinates of the row of the previous and current position remain the same. However, column index changes, I,e. previous position col index + 1 = current position 
- When the agent takes a left move(L), the coordinates of the row of the previous and current position remain the same. However, column index changes, I,e. previous position col index -1 = current position 
- When the agent takes an up move(U), the coordinates of the column of the previous and current position remain the same. However, row index changes, I,e. previous position row index - 1 = current position 
- When the agent takes a down move(D), the coordinates of the column of the previous and current position remain the same. However, row index changes, I,e. previous position row index + 1 = current position 


### Part 2: arrange_pichu.py:  add_pichu function
- A total of 8 loops are implemented to add an optimal solution if it exits one. 

Loop 1: Down to Up: To check all columns above,  we iterate from row to 0

Loop 2: Up to Down: To check all columns below, iterate from row to len(house_map)

Loop 3: Left Up Diagonal: To check this, iterate from col to 0.

Loop 4: Left Down Diagonal: To check this, iterate from col to 0.

Loop 5: Right to Left: To check this, iterate from col to 0

Loop 6: Right Up Diagonal: To check this, iterate from col to len(house_map[0])

Loop 7: Right Down Diagonal: To check this, iterate from  col to len(house_map[0])

Loop 8: Left to Right: To check this, iterate from col to len(house_map[0]). 

## Challenges Faced

- Debugging in python was my biggest challenge. Since I am not a regular python coder, dealing with loops was difficult, especially indexing the matrix. I was miss calculating a lot of indexes, which consumed a lot of time.

## Experimental Results 
1. route_pichu: map1.txt
<img width="518" alt="Screen Shot 2022-09-16 at 1 50 34 PM" src="https://media.github.iu.edu/user/21060/files/3826a782-4ee7-420f-974f-a1e1bf3b9262">

2. route_pichu: map2.txt
<img width="509" alt="Screen Shot 2022-09-16 at 1 52 53 PM" src="https://media.github.iu.edu/user/21060/files/cd65a084-2b3c-4416-8ebf-cbeedf56cf46">

3. arrange_pichu: map1.txt, k =7
<img width="539" alt="Screen Shot 2022-09-16 at 2 42 53 PM" src="https://media.github.iu.edu/user/21060/files/64ae2268-e9a1-4d5a-9b68-2aa16e5a0784">


4. arrange_pichu: map1.txt, k =8
<img width="596" alt="Screen Shot 2022-09-16 at 1 56 59 PM" src="https://media.github.iu.edu/user/21060/files/a3758bce-8bb4-4503-b43a-52ef7ed9c912">

5. arrange_pichu: map2.txt, k =5
<img width="555" alt="Screen Shot 2022-09-16 at 1 57 09 PM" src="https://media.github.iu.edu/user/21060/files/f531c8a3-24d2-479d-9654-f1a5aa4484ab">

6. arrange_pichu: map2.txt, k = 8
<img width="536" alt="Screen Shot 2022-09-16 at 1 57 22 PM" src="https://media.github.iu.edu/user/21060/files/6bd5be30-6d23-4ce6-8208-34bee2c85b95">


## State space, Initial state, Goal state, Successor function, and Cost function
### Part 1: route_pichu
**State Space:**"p" can only move through "." and not through "X" and reach destination "@"

**Initial state:** "p" in the starting position in the map  

**Goal State:** "p" reaching destination node "@" by taking the shortest path and not hitting any obstacles.

**Successor Function:** Taking a step such that it does not hit an obstacle "X" and its moving in only 4 directions( U, D, R or L) 

**Cost Function:** The total cost will be the total number of steps taken to reach the goal state.


### Part 2: arrange_pichu
**State Space:**"p" can only be placed in "." and not in "X" and "@"

**Initial state:** One "p" in the map 

**Goal State:** K number of "p"'s in the map such that none of the "p"'s can see each other (row wise, column wise and diagonally)

**Successor Function:** Placing "p" in such a way that other "p"s can see each other and it doesn't have any "p"'s in the same row, column, or diagonally.

**Cost Function:** The total cost will be the product of the total number of "p"s placed and the cost of placing one "p", assuming that the cost for placing each "p" is the same. 
