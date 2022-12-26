# Assignment 3
## Part-1
### Part-of-speech tagging

#### Problem Statement:
The goal is to implement parts of speech tagging using the following algorithm.
- Naive Bayes (SIMPLE)
- Viterbi (HMM)
- MCMC (Complex)

#### Data:
- Data is split into bc.train and bc.test. 
- The train dataset consists of about 50,000 sentences. 
- Each sentence is followed by an parts of speech:ADJ (adjective),ADV (adverb), ADP (adposition), CONJ (conjunction), DET (determiner), NOUN, NUM (number), PRON (pronoun), PRT (particle), VERB, X (foreign word), and . (punctuation mark).

#### Algorithms:
 <img width="793" alt="Screen Shot 2022-12-04 at 7 57 54 PM" src="https://media.github.iu.edu/user/21060/files/f138b7d5-57bc-40ae-8270-702d7ea9ce10">

**1. Naive Bayes Algorithm: (SIMPLE)**
- Naive Bayes is a straightforward supervised machine learning technique that obtains results by applying the Bayes theorem to a set of features under the strict assumption of independence. 
- The algorithm takes the independence of each variable for granted by being ignorant about the real-world data which can lead to inaccurate predictions. 
- It is estimated by taking the maximum posterior probability of the given term which is P(word| parts of speech)

**Implementation/Design Decisions of Naive Bayes Algorithm**
- First, we calculated the number of times each part of speech is occurring for each word in the dataset and their probabilities and stored the same in the dictionary. 
- The posterior probability of each work is calculated as follows: P(tag|word) = (P(word|tag) * P(tag))/P(word).
- However, we ignore the P(word) and the equation gets updated as : P(tag|word) = (P(word|tag) * P(tag))
- The posterior probability of all word-tag is : P(tag1|word1)*P(tag2|word2)…P(tag_n|word_n) α (P(word1|tag1) * P(tag1)) * (P(word2|tag2) * P(tag2)) ….. (P(word_n|tag_n) * P(tag_n))
- While testing we return the tag with maximum probability for each word in the test sentence. 
- If the word is not present in the dictionary, then we return the part of speech with is prominent in the training dataset. 

**2. Viterbi Algorithm(HMM)**
- In the context of Markov information sources and hidden Markov models, the Viterbi algorithm is a DP method for determining the highest posterior probability.
- It estimates the most likely sequence of hidden states referred to as the Viterbi path (HMM).

**Implementation/Design Decisions of Viterbi Algorithm**
- We created two lists, one for initial probability and the other for transition probability. 
- Initial probability is a 1D list that stores the probability of occurrence of each part of speech.
- The transition probability is stored in a 2D array where we fixed every first word in the sentence and then calculate the transition probability with respect to previous words. 
- In a hidden Markov chain, the likelihood of each component is dependent on the preceding state (transition probability), and the probability of each word is dependent on the hidden state. 
- Given a set of words and hidden states (tags), the likelihood that they will occur is calculated by the following equation:  Probability = [P(tag1)P(word1|tag1)] [P(word2|tag2)P(tag2|tag1)]…. [P(wordn|tag_n)*P(tag_n|tag_n-1)]
- If the word is not present in the list then we have fixed a very small value as its probability and continued the calculation.  

**3. MCMC(Complex)**
- It is a method for taking samples from a probability distribution and calculating the desired quantity using those samples. In other words, it makes use of unpredictability to infer some relevant deterministic quantity.
- An arbitrary pattern of tags is initialized for the given sentence, and from this pattern, beginning from the initial tag, the values are altered for each tag. 
- The associated joint probability is then estimated using the "joint probability" function while preserving the fixed position of all other tags. Subsequently, using the function random.choice, a random tag is fixed at the place. 
- The same procedure is then carried out for each tag in the tag sequence, producing one sample. A number of samples from the given probability distribution are created by selecting the number of iterations and burning iterations (samples to discard initially). 
- We have selected the tag that appears the most frequently at each place in the data in order to determine the sequence.

**Implementation/Design Decisions of MCMC**
- The complex probability of a state depends on the two states that came before it, and the emission probability of each word depends on the hidden state. 
- The formula for calculating the likelihood of a given word order is the following:
Probability = [P(tag1)P(word1|tag1)] [P(word2|tag2)P(tag2|tag1)] [P(word3|tag3)P(tag3|tag2,tag1)]… [P(wordn|tag_n)*P(tag_n|tag_n-1,tag_n-2)]

#### Results
- The following are the results we obtained using bc.test dataset for the following models:

**1. Simple:**
```
Ground Truth:      Words Correct:          100.00%
Growth Truth:      Sentences Correct:      100.00%
Simple:            Words Correct:           93.95%     
Simple:            Sentences Correct:       47.50%
```
**2. HMM:**
```
Ground Truth:      Words Correct:          100.00%
Growth Truth:      Sentences Correct:      100.00%
HMM:               Words Correct:          91.87%     
HMM:               Sentences Correct:      40.55%
```
**3. Complex:**
```
Ground Truth:         Words Correct:          100.00%
Growth Truth:         Sentences Correct:      100.00%
Complex:              Words Correct:           88.91%     
Complex:              Sentences Correct:       40.55%
```

**Observations:**
- The accuracy of the Complex algorithm should be the highest. However, in our case, the word correct is highest for the Simple algorithm with an accuracy of 93.95%, followed by HMM algorithm with an accuracy of 91.87%. 
- The least work correct is for the Complex algorithm with an accuracy of 88.91%. 
- The sentences correct is highest for Simple with 47.50% and least for Complex and HMM with 40.55%

The following is the posterior probabilities and observations:
<img width="1008" alt="Screen Shot 2022-12-04 at 7 30 02 PM" src="https://media.github.iu.edu/user/21060/files/d4efe372-c0c1-43ee-9846-3ce3666c7912">

**Observations:**
- Simple and HMM return the highest value of their probabilities for their own solutions.
- However, this may not always be the case with Complex(when it doesn't converge) because it is a probabilistic model. 

