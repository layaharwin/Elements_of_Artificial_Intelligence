## Part 1

### Problem Statement
- Five birds, each carrying a different number from 1 to N, are seated on a power line. 
- They begin in a random sequence, and their objective is to quickly rearrange themselves so that they are in order from 1 to N. 
- One bird can swap places with another bird in its immediate vicinity exactly once in any one step.

### Algorithm used
- We have used A* algorithm to solve the problem
- BFT is not optimal beacuse want to grow the node in FRINGE with the least expensive path rather than the one with the shortest path from the initial state.
- So, we used Best first search with Algo #2 implemented using priority queue. We also stores g(s) which is the cost of the path from initial state to s

State Space: Includes every configuration that 1 to N birds can take.

Initial State: The first grouping of birds in the problem file

Successor Function: We swap only adjacent birds in a single step. 

Goal State: We arrange the birds in the following format -> 1-N  using the least number of moves (eg: 12345)

Cost Function: In Best First Search, the cost function is defined as:
f(s) = g(s) + h(s), where g(s) is is the cost of the path from initial state to s and h(s) is an admissible heuristic function


Heuristic Used: Number of misplaced tiles/2
- Initially we used number of misplaced tiles as our heuristic function. However it was overestimating the cost in some cases like :
- Eg: 1,2,4,3,5 , Here the heuristic function returns 2 as the answer, however we need only 1 swapping to reach the goal state. Hence it was over estimating the cost.
- So, avoid this, we updated our heuristic function as No of Misplaced Tiles/2
- This doesnt overestimate the cost for any state s. 


### Design Decisions
- Following is the psuedo code of the algorithm used:

      If GOAL_STATE == INITIAL_STATE? then return INITIAL_STATE

      INSERT(INITIAL_STATE, FRINGE)

      Repeat:

          If FRINGE == empty then return empty list
  
          Remove s from FRINGE
  
          If GOAL_STATE == s then return path
  
          For every state s' in SUCC(s):
  
              INSERT(s', FRINGE)
    
    
## Part 2:

### Problem Statement:
- Given an input-board-filename containing a board configuration, complete the function called solve(),  which should return a  list of valid moves.

### Algorithm Used:
Here, we have used the A* algorithm.
We have used a priority queue for FRINGE which will help us in popping the state with minimum cost.

State State: All the possible configurations of how 25 puzzle can be arranged

Initial State: The initial puzzle in  the problem file

Goal State: All the elements in the 25 puzzle arranged is arranged sequentially from 1 to 25

Cost Function:
Uniform 

Successor Function: 

The following moves are possible : 

- Move Row Right => R1, R2, R3, R4 and R5

- Move Row Left => L1, L2, L3, L4 and L5

- Move Up => U1, U2, U3, U4 and U5

- Move Down => D1, D2, D3, D4 and D5

- Move clockwise => Oc, Ic

- Move counter-clockwise => Occ, Icc

Heuristic Function:

- Trial 1: Initially, we tried the number of misplaced numbers in the puzzle. However, it was overestimating the cost in some scenarios. 

- Trial 2: Next, we tried the number of misplaced numbers in the puzzle/2. However, it wasn’t giving us the expected results

- Trial 3: We tried Manhattan distance. Here also we were not getting the expected results

- Trial 4: We also tried Manhattan distance/2. However, we still were not getting the expected results

- Trial 5: Then we tried Manhattan distance + number of misplaced numbers in the puzzle. Here also we were not getting the expected results 

- Trial 6: Finally, we moved forward with Manhattan. This heuristic function is working for board0 but its taking too long for board1


### Design Decisions:
The algorithm works are following:

      Define the valid states

      INSERT(INITIAL_STATE, other information) to  FRINGE

      Repeat:

          If FRINGE == empty then return empty list
  
          Remove s from FRINGE which has the lowest cost
  
          If GOAL_STATE == s then return path
  
          For every state s' in SUCC(s):
  
              INSERT(s', FRINGE)


## Part 3
### Problem Statement 
- We need to find the best route based on the chosen cost function, which provides the number of segments, miles, hours for a car driver, and anticipated hours for the delivery driver 
- We need to write a code that takes care of road networks containing errors and inconsistencies, just like any real-world dataset.

### Algorithm Used:
- The algorithm used is A*
- We have used a priority queue for FRINGE which will help us in popping the state with minimum cost.

Initial State: In start-city

Goal State: Reaches end-city from start-city

State space: All the cities from the start point that are mentioned in road-segments.txt

Successor Function: All the cities mentioned in road-segments.txt that are connected to the city which we are expanding. 

Edge Weights and cost:  Following is the edge weight for different cost_function
      segments: The edge cost for every segment is uniform. i.e 1 for each segment
      distance: The edge cost for each segment will be its distance in miles
      time: The edge cost for each segment will be its distance in miles divided by its speed limit in miles per hour.
      Delivery: The edge cost for each segment will be its distance in miles divided by its speed limit in miles per hour. 

Heuristic Function:
Distance: 
- Here we are finding the shortest path from the start to the end city. 
- Initially, we used the Haversine heuristic function. It estimates the shortest distance between cities using their longitudes and latitudes. However, in some of the cases it was overestimating the cost. 
- Hence, we changed our heuristic function to Haversine distance/ 2

Segments:
- Here we are finding the path from start to end city by taking the minimal number of segments
- Trial 1: Initially, we used the Haversine heuristic function. However, in some of the cases, it was overestimating the code.
- Trial 2: We then changed the heuristic function to Haversine distance/ 923. Here 923 is the largest segment length. However, we were not getting expected results
- Trial 3: Finally we changed the heuristic to (Haversine distance/ 923)/2.5 where 2.5 is the scaling factor. The scaling factor was determined using the trial and error method. 

Time:
- Here we are finding the path from start to end city which takes the minimum time.
- Time taken for each segment is calculated by distance in miles divided by its speed limit in miles per hour. 
- Initially, we tried the heuristic function Phaversine distance divided by 65. Here 65 is the highest speed. However, we were not getting the expected results.
- So, we changed the heuristic to (haversine_distance/65)/60, where 60 is the scaling factor which was found using trial and error

Delivery:
- Here we are finding the path from start to end city which minimizes the time at the same time drops a package if the speed limit is more than 50.
- We used the same heuristic function, used for time here. 
- Heuristic function is (haversine_distance/65)/60, where 60 is the scaling factor which was found using trial and error


### Design Decisions
The algorithm works are following:

      Calculate cost and Heuristic Function

      INSERT(INITIAL_STATE, other information) to  FRINGE

      Repeat:

          If FRINGE == empty then return empty list
  
          Remove s from FRINGE which has the lowest cost
  
          If GOAL_STATE == s then return path
  
          For every state s' in SUCC(s):
  
              INSERT(s', FRINGE)
