# SeekTruth.py : Classify text objects into two categories
#
# Team: shahds-jrateria-lharwin
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys

def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#
def classifier(train_data, test_data):
    # This is just dummy code -- put yours here!
    # Cleaning of data 
    # Removing . , ! ; and ?
    for i in range(0, len(train_data["objects"])):
        train_data["objects"][i]= train_data["objects"][i].replace(".","").replace(",","").replace("!","").replace(";","").replace("?","").replace(":", " ")

    Wi_A_count= {}
    Wi_B_count= {}
    total_A=0
    total_B=0

    for i in range( 0, len(train_data["objects"])):
        if train_data["labels"][i] == 'deceptive':  #deceptive', 'truthful
            for j in train_data["objects"][i].split():
                if j in Wi_A_count:
                    Wi_A_count[j]+=1
                else:
                    Wi_A_count[j]=1
#                total_A+=1
        else:
            for j in train_data["objects"][i].split():
                if j in Wi_B_count:
                    Wi_B_count[j]+=1
                else:
                    Wi_B_count[j]=1
#                total_B+=1

    Wi__A_count={}
    Wi__B_count={}
    for i in Wi_A_count.keys():
        if Wi_A_count[i]<5:
            Wi_A_count[i]=0
        else:
            Wi__A_count[i]= Wi_A_count[i]
            total_A+=Wi_A_count[i]

    for i in Wi_B_count.keys():
        if Wi_B_count[i]<5:
            Wi_B_count[i]=0
        else:
            Wi__B_count[i]=Wi_B_count[i]
            total_B+=Wi_B_count[i]

    total_para_A= train_data["labels"].count("deceptive")
    total_para_B= train_data["labels"].count("truthful")
    P_A= total_para_A/(total_para_A+ total_para_B)
    P_B= total_para_B/(total_para_B + total_para_A)
    Prob_Wi_A={}
    Prob_Wi_B={}
    
    for i in Wi__A_count.keys():
        Prob_Wi_A[i]=Wi__A_count[i]/total_A
    
    for i  in Wi__B_count.keys():
        Prob_Wi_B[i]=Wi__B_count[i]/total_B
    
    result=[]
    for i in range(0, len(test_data["objects"])):
        final_A=1*P_A
        final_B=1*P_B
        test_data["objects"][i]= test_data["objects"][i].replace(".","").replace(",","").replace("!","").replace(";","").replace("?","")
        for j in test_data["objects"][i].split():
            if j in Prob_Wi_A:
                final_A*=Prob_Wi_A[j]*1000
            elif j not in Prob_Wi_A:
                final_A*=(1/(total_A))*1000
            if j in Prob_Wi_B:
                final_B*=Prob_Wi_B[j] *1000
            elif j not in Prob_Wi_B:
                final_B*=(1/(total_B))*1000
        if final_B!=0 and final_A/final_B > 1:
            result.append("deceptive")
        else:
            result.append("truthful")        
    
    return result # [test_data["classes"][0]] * len(test_data["objects"])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
