# lharwin-a4

## Part 1 :  K-Nearest Neighbors Classification

### Problem Statement: 
- The goal is to implement a k-nearest neighbors classifier from scratch. 

### Algorithm : K-Nearest Neighbors Classification:
- The k-nearest neighbor's algorithm sometimes referred to as KNN, is a supervised learning classifier that employs proximity to produce classifications or predictions about the grouping of a single data point. 
- Although it can be applied to classification or regression issues, it is commonly employed as a classification algorithm because it relies on the idea that comparable points can be discovered close to one another.
- A class label is chosen for classification problems based on a majority vote, meaning that the label that is most commonly expressed around a particular data point is used.

### Files:
```utils.py: ```
- The ML algorithms will use the essential utility functions found in the utils.py file.

```k_nearest_neighbors.py: ```
- It contains a  KNearestNeighbors class in which the KNN algorithm is implemented.

### Implementation:
```utils.py file :```
- Completed the function euclidean_distance.
- Euclidean distance: It is defined as the square root of sum of squared differences between two vectors as shown below:
- euclidean_distance= sqrt(sum( for i to N square (a1[i] – a2[I])))
- Completed the function manhattan_distance. 
- Manhattan distance: It is defined as the sum of the absolute diff of the two vectors as shown below:
- manhattan_distance= sum (for i to N sum |a1[i] – a2[I]|))

```k_nearest_neighbors.py file :```

In fit(X, y): 
- We assign X(Input data) and y(True class values) to self._X and self._y respectively.

In predict(X): 

#### Step 1: Calculate distance[i][j]
- We first calculate the distance for each test sample(X[i]) to all the training samples(_X[j]) and store them into a 2D matrix distance. 
- It basically contains the distance between the test and train samples in the dataset. 
- Which distance to choose depends on the l1 or l2 metric, if the metric is l1 then it's manhattan_distance else it's euclidean distance (l2). 

#### Step 2: Find k nearest neighbors and their distances
- We iterate through the test data and store all class values of sorted neighbors(wrt distance) from indexes 0 to self.n_neighbors(number of neighbors) in neighbors array. 
- We also store their distances in neighbors_distance array(This is used while running weighted distance model). 

#### Step 3: Finds a predicted class for each test sample
Case 1: When weights are “uniform” : 
- We simple do majority vote of the k nearest neighbors of each test sample; Basically, the test sample is assigned the data class which has the most representatives within the k nearest neighbors of the sample. 
- We iterate over each test sample and finds all the unique class neighbors with their count. Finally, we assign the class whose frequency is highest among all as Y_prediction[j]. 

Case 2 : When weights are “distance” : 
- Here, we assign weights proportional to the inverse of the distance from the test sample to the neighbor
- We iterate over each test sample, create a dictionary to store the unique class neighbors and their weighted distance. We keep adding the weighted distance for each class in proportional to the inverse of the distance from the test sample to the neighbor. In denominator, we add a small value of 0.0000001to avoid divide by zero error(This can occur when the distance is 0).

### Difficulties/ Challenges faced:
- I mainly faced challenge while calculating the weighted distance. Initially, I was unaware how to handle that scenario, but I finally got it after thinking for a while.
- I also faced some issue with numpy array manipulation but was able to resolve it ultimately.

### Results:

```
The following are the screenshot of the output in the terminal:
```
<img width="862" alt="Screen Shot 2022-12-14 at 4 44 38 PM" src="https://media.github.iu.edu/user/21060/files/f937f6aa-c63c-4be7-bda8-04b7a455d178">

```
The following is the screenshot of the output of first few models for knn_digits_results. We can see that the results matches for my model and sklearn.
``` 
<img width="563" alt="Screen Shot 2022-12-14 at 4 45 47 PM" src="https://media.github.iu.edu/user/21060/files/3ec86b9b-af4a-42e7-a37a-d046e4ae9def">

```
The following is the screenshot of the output of first few models for knn_iris_results. We can see that the results  matches for my model and sklearn.
``` 
<img width="566" alt="Screen Shot 2022-12-14 at 4 46 42 PM" src="https://media.github.iu.edu/user/21060/files/7d55e25f-d1b8-478b-a101-ac6d87a6c510">


### Please Note: 
- I have implemneted only KNN algothm. However I have committed other files like multilayer_perceptron.py into my repository. 
- Also I have uploaded my output html files : k_nearest_neighbors.py and knn_digits_results.html  and __pycache__ folder. 
