__author__ = 'ashokmarannan'
import sys
import os
import math
import random
from globals import *
from get_data import get_data, get_attributes_value, get_attributes_label, stop_jvm
weights = []
tot_features = 0
sortedout={}
#from get_entropy import get_class_entropy
#from decision_tree import decision_tree, build_decision_tree

def populate_data():
    global data_set, attributes_list, attributes_label, class_label,firstclass,secclass,weights,tot_features
    
    data_set = get_data(data_set_file);
    attributes_list = get_attributes_value(data_set_file)
    
    attributes_label = get_attributes_label(data_set_file);
    attributes_label.append('bias')
    #print attributes_label
    firstclass = attributes_list['Class'][0];
    secclass = attributes_list['Class'][1];
    ##print firstclass
    #print secclass
    class_label = attributes_list['Class']
    tot_features = len(attributes_label)
    #print data_set
    #print attributes_list
    #print attributes_label
    #print class_label

def get_input():
    global data_set_file
    global n, l, e
    data_set_file = sys.argv[1]
    if(os.path.isfile(data_set_file) == False):
        print "Error: data set %s cannot be opened",(data_set_file)
        sys.exit(0)
    try:
        n = int(sys.argv[2])    #fold
        l = float(sys.argv[3])  #learning rate
        e = int(sys.argv[4])    #epoc    
        
    except ValueError:
        print("Error: getting input")
        sys.exit(0)

    ##print "data set file = " + data_set_file
    #print "n = " + str(n)
    #print "l = " + str(l)
    #print "e = " + str(e)

    return 0

def startify_data():
    global no_pos, no_neg, no_inst_per_fold
    global n, l, e
    global data_folds
    global pos_ratio
    global neg_ratio,firstclass,secclass
    fold = []

    for i,item in enumerate(data_set):
        #print item
        if item["Class"] == secclass:
            #print "Negative"
            no_pos = no_pos + 1
            positive_set.append((i,item))
        elif item["Class"] == firstclass:
            #print "Positive"
            no_neg = no_neg + 1
            negative_set.append((i,item))
    
    #print "positives " + str(len(positive_set))
    #print "negatives " + str(len(negative_set))

    #print positive_set
    #print negative_set
    random.shuffle(positive_set)
    random.shuffle(negative_set)
    no_inst_per_fold = len(data_set)/n
    #print "no of instances per fold "+ str(no_inst_per_fold)
    
    pos_ratio = (no_pos) / n
    neg_ratio = (no_neg) / n
    #print pos_ratio
    #print neg_ratio
    
    pos_no_per_fold = pos_ratio
    neg_no_per_fold = neg_ratio

    #print "pos_no_per_fold " + str(pos_no_per_fold)
    #print "neg_no_per_fold " + str(neg_no_per_fold)

    
    pos_count = 0;
    neg_count = 0;
    
    for no in range(n):
        fold = []
        for i in range(pos_no_per_fold):
            fold.append(positive_set[pos_count])
            pos_count = pos_count + 1;
        
        for j in range(neg_no_per_fold):
            fold.append(negative_set[neg_count])
            neg_count = neg_count + 1;
        
        data_folds.append(fold)
    #print pos_count
    #print neg_count
    for i in range(len(positive_set) - pos_count):
        data_folds[i].append(positive_set[pos_count+i])
    for i in range(len(negative_set) - neg_count):
        data_folds[i].append(negative_set[neg_count+i])
    for i in data_folds:
        random.shuffle(i)
    #print "length of data folds " + str(len(data_folds))
    #print "length of data folds 1 " + str(len(data_folds[0]))
    #for i in range(len(data_folds)):
    #    for listoftup in data_folds[i]:
     #       print listoftup[0]
            
    return

def predict_test_data(root):
    global test_set_data
    counter = 0
    print "<Predictions for the Test Set Instances>"
    for element, instance in enumerate(test_set_data):
        predicted_class = root.class_predict(instance)
        actual_class = instance['class']
        print "{2}: Actual: {1} Predicted: {0}".format(predicted_class, actual_class, element+1)
        if (predicted_class == actual_class):
            counter = counter + 1


    print "Number of correctly classified: {0}, total test instances: {1}".format(counter ,len(test_set_data))
    return 0

def get_sigmoid(x):
    return (1.0)/(1.0 + math.exp(-x))

def calculate_output(training_instance):
    #instance_wt = 
    #print training_instance
    inputs = training_instance[1]
    inputs = {key:val for key,val in inputs.items() if key!='Class'}
    inputs['bias']=1
    #inputs = inputs.values()
    #inputs = inputs+[1]
    #print type(weights[0])
    output=0
    #print inputs
    for i in attributes_label:
        out = (inputs[i]*weights[i])
        #print out
        output+=out
    output= get_sigmoid(output)
    #print output
    return output
def evaluate_instance(instance,foldno):
    oj = calculate_output(instance)
    output=0
    if (oj>0.5):
        output = secclass
    else:
        output = firstclass
    global sortedout
    sortedout[instance[0]] = (foldno,output,instance[1]['Class'],oj)
    #print "{0} {1} {2} {3}".format(instance[0],output,instance[1]['Class'],oj)
    return 1 if output == instance[1]['Class'] else 0
def calculate_error(trainingset):
    for epochno in range(e):
        for instance in trainingset:
            oj = calculate_output(instance)
            #print oj
            
            actual_o = instance[1]['Class']
            actual_o = 0 if actual_o==firstclass else 1
            instance = instance[:]
            instance[1]['bias']=1
            error = oj*(1-oj)*(actual_o - oj)
            errl=error*l
            for label in weights:
                weights[label]+=errl*instance[1][label]
            #print weights
            #print weights['bias']
def main():
    #global train_set_data, test_set_data, attributes_lables, attributes_nom_values,
    #global class_labels
    global weights
    get_input()
    populate_data()
    startify_data()
    #print 'stratified'
    
    tot_cur=0
    tot=0
    for foldno in range(n):
        training_set=[]
        weights = {i:0.1 for i in attributes_label}
        weights['bias']=0.1
        
        test_set = data_folds[foldno]
        for i in range(n):
            if i==foldno: continue
            training_set.extend(data_folds[i])
        
        #print data_folds[0][0]
        calculate_error(training_set)
        for instance in test_set:
            tot+=1
            tot_cur+=evaluate_instance(instance,foldno)
        #print [instance[0] for instance in training_set]
        #print [instance[0] for instance in test_set]
        
    #print 'done'
    #print tot_cur
    for i in range(len(data_set)):
        print " ".join(str(val) for val in sortedout[i])
    #print float(tot_cur)/tot
    stop_jvm()
    return 0

if __name__ == "__main__":
    main()