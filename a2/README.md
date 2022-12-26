# Assignment 2

## Part 1: Raichu Board Game - Minimax implementation with Alpha-beta pruning

State Space: The state space is the set of all possible positions for the Pichu, Pikachu, and Raichu on a NxN board (N >= 8).

Initial State: The first board setup before any player starts paying their turn, the initial state is also the state given in the PDF for Assignment 2.(for testing purposes)

Goal State: When the opposing player has used up all of their pieces i.e the opposing player has 0 total pieces remaining you, the board is in the goal state.

Successor Function: Function that takes into consideration the present player and the state of the board and produces a list of potential future moves that can be made to the board given the constraints on piece movement(next moves of Pichu, Pikachu, and Raichu) is the successor function.

Algorithm Used: Minimax with Alpha-Beta pruning.


### Brief Solution Description:

The problem is analogous to chess and can serve as a foundation for future development. We utilized the minimax method in conjunction with alpha-beta pruning to overcome this issue. We limited the maximum depth to 3 since anything more complicated caused the code to run slowly and produce unsatisfactory results (or any result at all).

We improved the running time by utilizing 'yield' and 'itertools' to produce successors since they build successor states asynchronously and need less computation when states don't need to be examined as a result of pruning.

In order to accomplish this, it utilizes both the min and max functions, traversing the tree a further +1 depth and extracting the minimum and maximum values of beta and alpha for the min script, respectively.When the maximum depth or a goal state is reached, the algorithm will end this min/max back and forth and output the move that gives the maximum evaluation function value.When the opponent has no more pieces on the board, they are in a goal state.

Each element was given an importance value for the heuristic, and we utilized those values to determine our own and the adversary's scores. The value is then returned as a heuristic after we deduct these scores.

We choose to utilize minimax at a max depth of 3 with alpha-beta pruning in order to reduce run times because the description of the game satisfies all of the criteria for an adversarial search based game (two players, turn taking, 0 sum, time limits, etc.). We had to choose an evaluation function for the minimax algorithm to employ in order to evaluate each state differently based on the player. We chose to employ a weighted evaluation function, which assigned weights to the variation in the number of each unique item. The algorithm would be driven to attempt to reduce the oppositions between raichu pieces over a pichu piece, for example, because the more important parts (raichu) received more weights than the less important ones (pichu).

### References

1. https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/  #No Code was copied

### Problems, Assumptions, Decisions :
The most important decision was which assessment capability to use.In games like these, where different pieces have different effects (raichu can move more than pichu and pikachu, for example), a weighted evaluation function seemed like the best choice. For each piece, the number of pieces on the board that differs between players is determined, and that number is given a specific weight, with the more valuable pieces receiving more weight.We had to slightly alter the weights of each piece, but in the end we settled on 1 for Pichu, 5 for Pikachu, and 15 for Raichu.In certain states, such as the initial state, where a single move will not eliminate any pieces, our evaluation function will return 0 for the successors.To accommodate this, a brand-new component was added.
To determine how much mobility a move will provide in the future, it multiplies each player's total number of successors from the current state by 0.1.As a result, run times are definitely longer, especially for states with a lot of raichus.
Also we faced probem in parsing the Json file, where the file was used to store the most optimal solution but it was overcomed.



## Part 2:  Truth be Told

### Problem: 
Classify textual objects into “truthful” or “deceptive” using the Naive Bases classifier. This classifier often uses a bag-of-words approach, in which each item is only represented as an unordered "bag" of words without any knowledge of the document's grammatical structure or word order.

### Approach: 
1. Data Cleaning: Removed the following characters from the text : . , ! ; ? :
2. Created two dictionaries to keep track of the count the number of words in A and B 
3. Removed the words that occur less than 5 times. Choose 5 as our threshold as we were getting the best accuracy for 5 compared to other values we tried.
4. Calculated P(A) and P(B)
```
P(A)= Total number of objects that are “deceptive” / (Total number of objects that are “deceptive” + Total number of objects that are “truthful”)
P(B)= Total number of objects that are “truthful” / (Total number of objects that are “deceptive” + Total number of objects that are “truthful”)
```
5. Calculate likelihoods P(wi|A) and P(wi|B)
```
P(wi|A) = Number of times wi occurs in A/ Total number of words in A
P(wi|B) = Number of times wi occurs in B/ Total number of words in B
```
6. Calculate the following for all the objects in test_data:
![image](https://media.github.iu.edu/user/21060/files/3fe914ec-59bf-43a3-9bbf-038cad57ae21)
```
where,  
P(A|w1,w2...wn) = P(A)*P(w1|A)*P(w2|A)...*P(wn|A)
and
P(B|w1,w2...wn) = P(B)*P(w1|B)*P(w2|B)...*P(wn|B)
```
Few important points:
- We noticed that few of the probabilities were reaching 0, so to avoid that we multiplied all the probabilities with 1000 for both A and B. Since we are multiplying both the denominator and numerator, the effect cancels out. However, it helps us preserve our probabilities from reaching 0. We found the value 1000 using the trial and error method and compared to all other values we tested, 1000 is giving the maximum accuracy. 
```
Updated P(wi/A) and P(wi/B)
P(wi|A) = (Number of times wi occurs in A/ Total number of words in A) *1000
P(wi|B) = (Number of times wi occurs in B/ Total number of words in B) *1000
```

- When encountering a word, not in A or B, we multiplied the result with a constant. If the class we are checking is “truthful”, then the constant is (1/total number of words in B). If it's class “deceptive”, then the constant is (1/total number of words in A). We experimented with a lot of values and decided to go with a constant value that changes according to the number of words in train_data.
```
Updated P(wi|A) and P(wi|B) when wi is not present in A or B
P(wi|A) = (1/total number of words in A) *1000
P(wi|B) = (1/total number of words in B) *1000
```
7. Finally, if the ratio is greater than 1, then the object belongs to class “deceptive” and if the ratio is less than 1, then they belong to class “truthful” 

### Results:
Following is the screenshot of our result:

<img width="847" alt="Screen Shot 2022-11-11 at 8 10 15 PM" src="https://media.github.iu.edu/user/21060/files/2e5035cd-e37f-44e3-abff-f8c7e8f6f250">
**Accuracy Obtained: 86% **
