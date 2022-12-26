###################################
# CS B551 Fall 2022, Assignment #3
#
# Authors: Dhairya Shah(shahds), Jayat Rateria(jrateria) and Laya Harwin(lharwin)
#
# (Based on skeleton code by D. Crandall)
#


import random
import math
from random import randint
import numpy
from collections import Counter

new_w_s_count={}
max_s_part=''
transition_prob = [[0.00000000000000000000000000000000000000000001 for x in range(12)] for y in range(12)]
initial_prob=[0.00000000000000000000000000000000000000000001]*12
complex_prob=[[[0 for i in range(12)] for j in range(12)] for k in range(12)]

# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
class Solver:
    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    def posterior(self, model, sentence, label):
        value= 0.00000000000000000000000000000000000000000001
        s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
        pos={'adj':0,'adv':1,'adp':2,'conj':3,'det':4,'noun':5,'num':6,'pron':7,'prt':8,'verb':9,'x':10,'.':11}
        if model == "Simple":
            output=0
            for i in range(0, len(sentence)):
              x= sentence[i]
              if x not in new_w_s_count:
                temp1= s_list.index(label[i])
                output=output+math.log(value)+math.log(initial_prob[temp1])
              else:
                temp2= s_list.index(label[i])
                temp1=(new_w_s_count[sentence[i]][temp2]/10)
                if temp1==0:
                  temp3= s_list.index(label[i])
                  output=output+math.log(value)+math.log(initial_prob[temp3])
                else:
                  output=output+math.log(temp1)
            return output
        
       #     return -999
        elif model == "HMM":
            output=0
            for i in range(0, len(sentence)):
              if i==0:
                temp1= sentence[i]
                if temp1 not in new_w_s_count:
                  temp2= s_list.index(label[i])
                  output=output+ math.log(value)+math.log(initial_prob[temp2])
                else:
                  temp3= s_list.index(label[i])
                  temp4=(new_w_s_count[sentence[i]][temp3]/10)
                  if temp4==0:
                    temp5= s_list.index(label[i])
                    output=output+math.log(value)+math.log(initial_prob[temp5])
                  else:
                    temp6= s_list.index(label[i])
                    output=output+math.log(temp4)+math.log(initial_prob[temp6])
              else:
                temp1= sentence[i]
                if temp1 not in new_w_s_count:
                  temp2= s_list.index(label[i])
                  temp3= s_list.index(label[i-1])
                  output=output+math.log(value)+math.log(max(transition_prob[temp3][temp2],value))
                else:
                  temp5= s_list.index(label[i])
                  temp4=(new_w_s_count[sentence[i]][temp5]/10)
                  if temp4<=0:
                    temp2= s_list.index(label[i])
                    temp3= s_list.index(label[i-1])
                    output=output+math.log(value)+math.log(max(transition_prob[temp3][temp2],value))
                  else:
                    temp6= s_list.index(label[i])
                    temp7= s_list.index(label[i-1])
                    output=output+math.log(temp4)+math.log(max(transition_prob[temp7][temp6],value))
            return output
            #return -999
        elif model == "Complex":
            return self.joint_prob(sentence,label)
            #return -999
        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train(self, data):
        global transition_prob
        global initial_prob
        global max_s_part
        s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
        w_s_count={}
        total_no_of_words=0
        for i in range(0, len(data)):
            for j in range(0, len(data[i][0])):
                if data[i][0][j] in w_s_count:
                    index= s_list.index(data[i][1][j])
                    newlist= w_s_count[data[i][0][j]]
                    newlist[index]+=1
                    w_s_count[data[i][0][j]]=newlist
                else:
                    list1=[0]*12
                    index= s_list.index(data[i][1][j])
                    list1[index]+=1
                    w_s_count[data[i][0][j]]=list1
                total_no_of_words+=1

        max_s_list=[0]*12
        for i in w_s_count.keys():
            list1=w_s_count[i]
            for j in range(0, 12):
                max_s_list[j]+=list1[j]
        max_s_list1= max(max_s_list)
        max_s_list1_index= max_s_list.index(max_s_list1)
        max_s_part= s_list[max_s_list1_index]
        for i in w_s_count.keys():
            list1= w_s_count[i];
            sum1=0
            for j in range(0, 12):
                sum1+=list1[j]
            for j in range(0, 12):
                list1[j]=list1[j]/sum1
            new_w_s_count[i]= list1

        
        for i in range(0, len(data)):
            index= s_list.index(data[i][1][0])
            initial_prob[index]+=1
        for i in range(0, 12):
            initial_prob[i]= initial_prob[i]/(len(data))

        #transition_prob = [[0 for x in range(12)] for y in range(12)]
        for i in range(0, len(data)):
            prev= data[i][1][0]
            prev_index= s_list.index(prev)
            for j  in range(1,  len(data[i][0])):
                curr_index= s_list.index(data[i][1][j])
                transition_prob[prev_index][curr_index]+=1
                prev_index= curr_index
        n= len(data)
        for i in range(0,12):
            for j in range(0, 12):
                transition_prob[i][j]=(transition_prob[i][j])/(total_no_of_words-n)

        global complex_prob
        
        for j,k in data:
            for i in range(len(j)):
                if i>=2:
                    temp1= s_list.index(k[i-2])
                    temp2 = s_list.index(k[i-1])
                    temp3= s_list.index(k[i])
                    complex_prob[temp1][temp2][temp3]+=1
        
        for i in range(12):
            for j in range(12):
                temp1=sum(complex_prob[i][j])
                for k in range(12):
                    if temp1!=0:
                        complex_prob[i][j][k]/=temp1
        pass
 
    # Functions for each algorithm. Right now this just returns nouns -- fix this!
    #
    def simplified(self, sentence):
        s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
        out=[]
        for i in range (0, len(sentence)):
            if sentence[i] in new_w_s_count.keys():
                list1= new_w_s_count[sentence[i]]
                maxelement=max(list1)
                temp= list1.index(maxelement)
                s_element= s_list[temp]
                out.append(s_element)
            else:
                out.append(max_s_part)
        return out
        #return [ "noun" ] * len(sentence)

    def hmm_viterbi(self, sentence):
        s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
        out=[]
        dp=[[0.00000000000000000000000000000000000000000001 for x in range(12)] for y in range(len(sentence))]
        for i in range(0, 12):
            if sentence[0]  not in new_w_s_count:
                dp[0][i]= 0.00000000000000000000000000000000000000000001*initial_prob[i]
            else:
                list1= new_w_s_count[sentence[0]]
                prob= list1[i]
                dp[0][i]= prob*initial_prob[i]
        for w in range(1, len(sentence)):
            for s in range(0, 12):
                list1=[0]*12
                for k in range(0, 12):
                    if sentence[w] not in new_w_s_count.keys():
                        list1[k]= 0.00000000000000000000000000000000000000000001*transition_prob[k][s]* dp[w-1][k]
                    else:
                        list1[k]= new_w_s_count[sentence[w]][s] * transition_prob[k][s]* dp[w-1][k]
                dp[w][s]= max(list1)
        for i in range(0, len(sentence)):
            index= dp[i].index(max(dp[i]))
            out.append(s_list[index])
        return out
        #return [ "noun" ] * len(sentence)

    def calc_prob(self, sentence):
        x=0
        output=[]
        list_1=[[0 for j in range(12)] for i in range(len(sentence))]
        w1=sentence[0]
        s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
        for j in range(12):
          if w1 in new_w_s_count:
            list_1[0][j]=new_w_s_count[w1][j]
          else:
            list_1[0][j]=0
        
        temp2=[[0 for j in range(12)] for i in range(len(sentence))]
        output1=[]
        output1.append(s_list[list_1[0].index(max(list_1[0]))])

        for v in range(1,len(sentence)):
          for v2 in range(12):
            if sentence[v] in new_w_s_count:
              v1=new_w_s_count[sentence[v]][v2]
            else:
              v1=initial_prob[v2]
            for k in range(12):
              x=max(list_1[v][v2],list_1[v-1][k]*transition_prob[k][v2]*v1)
              if x>list_1[v][v2]:
                temp2[v][v2]=k
              list_1[v][v2]=x
          ind=list_1[v].index(max(list_1[v]))
          output1.append(s_list[ind])
        
        for i in range(len(sentence)-1,-1,-1):
          if i==len(sentence)-1:
            x=list_1[i].index(max(list_1[i]))
            output.append(s_list[x])
          else:
            p=temp2[i+1][x]
            output.append(s_list[x])
        return output1

    def joint_prob(self,sentence,labels):
      s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
      output=0
      val = 0.00000000000000000000000000000000000000000001
      for word in range(0,len(sentence)):
        if word==0:
          if sentence[word] not in new_w_s_count:
            temp1= s_list.index(labels[word])
            output=output+math.log(val)+math.log(max(val,initial_prob[temp1]))
          else:
            temp1= s_list.index(labels[word])
            output=output+math.log(max(val,new_w_s_count[sentence[word]][temp1]/10))+math.log(max(val,initial_prob[temp1]))
        elif word==1:
          if sentence[word] not in new_w_s_count:
            temp1= s_list.index(labels[word-1])
            temp2= s_list.index(labels[word])
            output=output+math.log(val)+math.log(max(val,transition_prob[temp1][temp2]))
          else:
            temp1= s_list.index(labels[word])
            temp2= s_list.index(labels[word-1])
            output=output+math.log(max(val,new_w_s_count[sentence[word]][temp1]/10))+math.log(max(val,transition_prob[temp2][temp1]))
        else:
          if sentence[word] not in new_w_s_count:
            temp1= s_list.index(labels[word])
            temp2= s_list.index(labels[word-2])
            temp3= s_list.index(labels[word-1])
            output=output+math.log(val)+math.log(max(val,transition_prob[temp3][temp1]))+math.log(max(val,complex_prob[temp2][temp3][temp1]))
          else:
            temp1= s_list.index(labels[word])
            temp2= s_list.index(labels[word-1])
            temp3= s_list.index(labels[word-2])
            output=output+math.log(max(val,new_w_s_count[sentence[word]][temp1]/10))+math.log(max(val,transition_prob[temp2][temp1]))+math.log(max(val,complex_prob[temp3][temp2][temp1]))
      return output


    def complex_mcmc(self, sentence):
        output=[]
        value = 0.00000000000000000000000000000000000000000001
        temp1=[ "adj" ] * len(sentence)
        list_1=[]
        num=10
        s_list=['adj','adv','adp', 'conj', 'det', 'noun', 'num', 'pron', 'prt', 'verb', 'x', '.']
        for i in range(20):
          v1=temp1
          v2=temp1
          list_2=[]
          for j in range(len(v1)):
            temp_dict={}
            temp_dict=temp_dict.fromkeys(s_list)
            for k in s_list:
              v2[0:len(list_2)]=list_2
              v2[j]=k
              prob=self.joint_prob(sentence,v2)
              temp_dict[k]=math.exp(j)
            if sum(temp_dict.values())!=0:
              temp_dict = {k1: v / t for t in (sum(temp_dict.values()),) for k1, v in temp_dict.items()}
              c = numpy.random.choice(list(temp_dict.keys()),1,list(temp_dict.values()))
            else:
              temp_dict = {k1: v / (value) for k1, v in temp_dict.items()}
              c = numpy.random.choice(list(temp_dict.keys()),1)
            c=c[0]
            list_2.append(c)
          if i>num:
              list_1.append(v1)
        output1=self.calc_prob(sentence)
        for i in range(len(list_1[0])):
          list_3=[]
          for j in range(len(list_1)):
            list_3.append(list_1[j][i])
          output.append(Counter(list_3).most_common(1)[0][0])
        return output1

    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence):
        if model == "Simple":
            return self.simplified(sentence)
        elif model == "HMM":
            return self.hmm_viterbi(sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence)
        else:
            print("Unknown algo!")

