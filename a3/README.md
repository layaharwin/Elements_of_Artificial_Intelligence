# shahds-jrateria-lharwin-a3
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

## Part-2
### AI Text Recognition - Implementation of HMM with MAP inference and Viterbi Algorithm

#### Brief Description of Problem
We divided this task into two different problems since this component required two distinct outputs (the Simple Bayes output and the HMM Viterbi output), with HMM serving as an extension of the Simple Bayes Net. Beginning with some text training data, we had to generate transition and starting state probabilities (which we decided to use bc.train). To determine the emission probability, we compared each training letter to each testing letter, comparing the ratio of accurate black and white characters to the total number of characters to determine which testing letter matched the training letter the closest.We then incorporated the emission probabilities, transition probabilities, and starting state probabilities into an HMM, generated a viterbi matrix, and backpropagated to determine the best output using MAP inference.

#### Simple
With this approach, we return the characters that have the highest emission probability of of all the characters that are provided. We also used laplace smoothing for the probability for new terms.

#### Initial Probability
Initial Probability is obtained by counting the instances of a letter being used as an initial letter and dividing that number by the total number of words in the training data.

#### Emission Probability
Comparing each pixel in the test and training sets of data yields the emission probability. We may compute it by [(1 - m)^matched * m^unmatched] after counting the number of matched and unmatched pixels and accounting for m% noise.

#### Transition Probability
The number of transitions between two letters is counted, and the transition probability is computed by dividing that number by the total number of occurrences of the first letter.

#### Viterbi
We build the Vlue_table and select_table tables for Viterbi. Then, we use the initial and emission probability to fill the first column. The remaining values are then calculated using the populated data and the transition probability. We return the most likely path via backtracking.

#### Problem and Assumptions
Choosing a text training dataset was our initial step, and we chose to utilize bc.train with POS removal. We had to decide if we wanted the initial state probabilities to be the chance that a phrase began with a given letter, which was a rather significant assumption to make when calculating the probabilities. We chose the first option since it provides us with more training scenarios. We chose to employ a weighted method for the emission probability since the results from a basic Bayes model were much improved.We tested and tuned several parameters before settling on the weights we used (0.6 & 0.4) vs (0.9 & 0.1). Since the emission probabilities performed so accurately in the simple bayes output, we chose to use a weighted based approach once more when incorporating the emission and transition probs into the viterbi algorithm, using the transition probs and the previous state vertibi outputs as additional components.
