# Assignment 2

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
