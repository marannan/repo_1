__author__ = 'ashokmarannan'
import sys
import os
import math
import random
import operator
from globals import *
from get_data import * #import get_data, get_attribute_values, get_attribute_names, start_jvm, stop_jvm


def populate_data():
    global train_set_data, test_set_data, attribute_names, attribute_values, class_names
    
    train_set_data = get_arff_data(train_set_file);
    test_set_data = get_arff_data(test_set_file);
    attribute_names = get_attribute_names_1(train_set_file)
    attribute_values = get_attribute_values(train_set_file);
    #attribute_values_2 = get_attribute_values_1(train_set_file);
    #attribute_values_1 = get_attribute_values_1(train_set_file);
    
    for attri in attribute_values:
        if attri == "class" or attri == "Class":
            class_values[attri] = attribute_values[attri]
    
    #debug_print(str(train_set_data)
    #debug_print(str(test_set_data))
    #debug_print(str(attribute_names))
    #debug_print(str(attribute_values))
    #debug_print(str(attribute_values_2))
    
    #for attri in attribute_names:
        #debug_print("attributes name:\n" + str(attri))

    #for attri_val in attribute_values:
        #debug_print("attributes values:\n" + str(attri_val) + str(attribute_values[attri_val]))
        
    return

def get_input():
    global train_set_file, test_set_file
    global nort
    
    try:
        train_set_file = sys.argv[1]
        if(os.path.isfile(train_set_file) == False):
            print "error: train set %s cannot be opened",(train_set_file)
            sys.exit(0)
            
        test_set_file = sys.argv[2]
        if(os.path.isfile(test_set_file) == False):
            print "error: test set %s cannot be opened",(test_set_file)
            sys.exit(0)    
    
       
        nort = str(sys.argv[3])    #n or t
        
    except ValueError:
        print("error: getting input") 
        sys.exit(0)

    #debug_print(str("input:"))
    #debug_print(str("train set file = " + train_set_file))
    #debug_print(str("test set file = " + test_set_file))
    #debug_print(str(nort))

    return 0

def find_prob_class(train_set_data):
    global y_1
    global y_2
    inst_total = len(train_set_data)
    
    for inst in train_set_data:
        if inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][0]:
            y_1 = y_1 + 1
        
        if inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][1]:
            y_2 = y_2 + 1    
    
    p_y_1 = float(y_1 + 1)/float(inst_total + 2)
    p_y_2 = float(y_2 + 1)/float(inst_total + 2)    
    
    class_count[class_values[class_values.keys()[0]][0]] = y_1
    class_count[class_values[class_values.keys()[0]][1]] = y_2
    
    
    return (p_y_1, p_y_2)

def find_prob_naive(test_attri, test_attri_val):
    global y_1, y_2
    x_y_1 = 0
    x_y_2 = 0
    inst_total = len(train_set_data)
    test_attri_val_count = len(attribute_values[test_attri])
    class_count = 2    
    
    for inst in train_set_data:
        #debug_print(str(test_attri) + " : " + str(inst[test_attri]) + " : "+ str(inst["class"]))
        if(inst[test_attri] == test_attri_val) and inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][0]:
            x_y_1 = x_y_1 + 1
                
        if(inst[test_attri] == test_attri_val) and inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][1]:
            x_y_2 = x_y_2 + 1        
      
    num_1 = x_y_1 + 1 
    den_1 = y_1 + test_attri_val_count
    p_x_y_1 = float(num_1)/float(den_1)
    
    
    num_2 = x_y_2 + 1 
    den_2 = y_2 + test_attri_val_count
    p_x_y_2 = float(num_2)/float(den_2)
    
    #debug_print(str(test_attri) + " : " +str(test_attri_val) + " count: " + str(x_y_1) + " " + str(p_x_y_1)) 
    #debug_print(str(test_attri) + " : " +str(test_attri_val) + " count: " + str(x_y_2)+ " " + str(p_x_y_2)) 
    
    return (p_x_y_1, p_x_y_2)


def find_prob_naive_tan(test_inst, test_attri, parent_list):
    global y_1, y_2
    x_y_1 = 0
    x_y_2 = 0
    x_p_1 = 0
    x_p_2 = 0
    inst_total = len(train_set_data)
    test_attri_val_count = len(attribute_values[test_attri])
    class_count = 2    
    
    for train_inst in train_set_data:
        #x/y
        if train_inst[test_attri] == test_inst[test_attri] and train_inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][0]:
            hit  = 0
            for parent in parent_list:
                if parent != -1:
                    if train_inst[attribute_names[parent]] == test_inst[attribute_names[parent]]:
                        hit = hit + 1
            if hit == len(parent_list) or parent == -1:
                x_y_1 = x_y_1 + 1
                
        if train_inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][0]:
            hit  = 0
            for parent in parent_list:
                if parent != -1:
                    if train_inst[attribute_names[parent]] == test_inst[attribute_names[parent]]:
                        hit = hit + 1
            if hit == len(parent_list) or parent == -1:
                x_p_1 = x_p_1 + 1
                
                
        #x/y'
        if train_inst[test_attri] == test_inst[test_attri] and train_inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][1]:
            hit  = 0
            for parent in parent_list:
                if parent != -1:
                    if train_inst[attribute_names[parent]] == test_inst[attribute_names[parent]]:
                        hit = hit + 1
            if hit == len(parent_list) or parent == -1:
                x_y_2 = x_y_2 + 1
                
        if train_inst[class_values.keys()[0]] == class_values[class_values.keys()[0]][1]:
            hit  = 0
            for parent in parent_list:
                if parent != -1:
                    if train_inst[attribute_names[parent]] == test_inst[attribute_names[parent]]:
                        hit = hit + 1
            if hit == len(parent_list) or parent == -1:
                x_p_2 = x_p_2 + 1                
        
        
                
      
    num_1 = x_y_1 + 1 
    den_1 = x_p_1 + test_attri_val_count
    p_x_y_1 = float(num_1)/float(den_1)
    
    
    num_2 = x_y_2 + 1 
    den_2 = x_p_2 + test_attri_val_count
    p_x_y_2 = float(num_2)/float(den_2)    
    
    
    #debug_print(str(test_attri) + " : " +str(test_attri_val) + " count: " + str(x_y_1) + " " + str(p_x_y_1)) 
    #debug_print(str(test_attri) + " : " +str(test_attri_val) + " count: " + str(x_y_2)+ " " + str(p_x_y_2)) 
    
    return (p_x_y_1, p_x_y_2)


def find_prob_tan(x_1, x_1_val, x_2, x_2_val, y):
    global y_1, y_2
    x_1_x_2_y = 0
    x_1_y = 0
    x_2_y = 0
    inst_total = len(train_set_data)
        
    for inst in train_set_data:
        #debug_print(str(test_attri) + " : " + str(inst[test_attri]) + " : "+ str(inst["class"]))
        if(inst[x_1] == x_1_val) and inst[x_2] == x_2_val and inst[class_values.keys()[0]] == y:
            x_1_x_2_y = x_1_x_2_y + 1
            
        if(inst[x_1] == x_1_val) and inst[class_values.keys()[0]] == y:
            x_1_y = x_1_y + 1
            
        if(inst[x_2] == x_2_val) and inst[class_values.keys()[0]] == y:
            x_2_y = x_2_y + 1        
                
    num_1 = x_1_x_2_y + 1 
    den_1 = len(train_set_data) + (len(attribute_values[x_1]) * len(attribute_values[x_2]) * len(class_values[class_values.keys()[0]]))
    p_x_1_x_2_Y = float(num_1)/float(den_1)
    
    
    den_2 = class_count[y] + (len(attribute_values[x_1]) * len(attribute_values[x_2]))
    p_x_1_x_2_y = float(num_1) / float(den_2)   
    
    num_2 = x_1_y + 1
    den_3 = class_count[y] + len(attribute_values[x_1])
    p_x_1_y = float(num_2) / float(den_3)
    
    num_3 = x_2_y + 1
    den_4 = class_count[y] + len(attribute_values[x_2])
    p_x_2_y = float(num_3) / float(den_4)
    
    p_x_1_x_2 = p_x_1_x_2_Y * math.log( (p_x_1_x_2_y/(p_x_1_y * p_x_2_y)), 2)
    
    #debug_print(str(x_1_x_2_y))
    #debug_print(str(x_1_y))
    #debug_print(str(x_2_y))
    #debug_print(str(p_x_1_x_2_Y)) 
    #debug_print(str(p_x_1_x_2_y))
    #debug_print(str(p_x_1_y)) 
    #debug_print(str(p_x_2_y))     
    #debug_print(str(p_x_1_x_2))     
    
    return p_x_1_x_2

                
def naivebayes():
    p_y_1 = 0
    p_y_2 = 0
    correct = 0

    for name in attribute_names:
        if name != class_values.keys()[0]:
            debug_print(str(name) + " " + "class")
   
    debug_print("")
    
    (p_y_1, p_y_2) = find_prob_class(train_set_data) 
    
    for inst in test_set_data:
        p_xs_y_1 = []
        p_xs_y_2 = [] 
        p_x_y_1 = 1
        p_x_y_2 = 1        
        #debug_print(str(inst))
        for attri in inst:
            if attri != class_values.keys()[0]:
                p_X_y_1, p_X_y_2 = find_prob_naive(attri, inst[attri])
                p_xs_y_1.append(p_X_y_1)
                p_xs_y_2.append(p_X_y_2)
         
        for item in p_xs_y_1:
            p_x_y_1 = float(p_x_y_1) * float(item)
        
        for item in p_xs_y_2:
            p_x_y_2 = float(p_x_y_2) * float(item)
    
    
        p_y_1_x = (float(p_x_y_1) * float(p_y_1)) / ((float(p_x_y_1) * float(p_y_1)) + (float(p_x_y_2) * float(p_y_2)))
        p_y_2_x = (float(p_x_y_2) * float(p_y_2)) / ((float(p_x_y_2) * float(p_y_2)) + (float(p_x_y_1) * float(p_y_1)))

       
        if p_y_1_x > p_y_2_x:
            debug_print(str(attribute_values[class_values.keys()[0]][0]) + " " + str(inst[class_values.keys()[0]]) + " " + str('{0:.16f}'.format(p_y_1_x)))
            if  str(attribute_values[class_values.keys()[0]][0]) == str(inst[class_values.keys()[0]]):
                correct = correct + 1            
        else:
            debug_print(str(attribute_values[class_values.keys()[0]][1]) + " " + str(inst[class_values.keys()[0]]) + " " + str('{0:.16f}'.format(p_y_2_x)))
            if  str(attribute_values[class_values.keys()[0]][1]) == str(inst[class_values.keys()[0]]):
                correct = correct + 1            
        
        
      
    debug_print("")     
    debug_print(str(correct))
        
        
    return 

def tan():
    p_y_1 = 0
    p_y_2 = 0
    correct = 0
    p_Xn_Y = []
    p_X_1_X_2_Y_l = []
    max_span_tree_name = {}
    max_span_tree_no = {}
    old_v_l = attribute_names
    new_v_l = []
    

    (p_y_1, p_y_2) = find_prob_class(train_set_data)
    
    #step 1: build attributes pair probability matrix
    for i in range(0, len(attribute_names) - 1):
        p_x_1_x_2_y_l = []
        for j in range(0, len(attribute_names) - 1):
            p_l = [] 
            p_x_1_x_2_y = 0               
            x_1 = attribute_names[i]
            x_2 = attribute_names[j]
            if i == j:
                p_x_1_x_2_y_l.append(-1.0)
            else:
                for x_1_val in attribute_values[x_1]:
                    for x_2_val in attribute_values[x_2]:
                        for y in class_values[class_values.keys()[0]]:
                            p_l.append(find_prob_tan(x_1, x_1_val, x_2, x_2_val, y))
            
                for p in p_l:
                    p_x_1_x_2_y = p + p_x_1_x_2_y
            
                p_x_1_x_2_y_l.append(p_x_1_x_2_y)
            
        #debug_print(str(p_X_1_X_2_Y))
        p_X_1_X_2_Y_l.append(p_x_1_x_2_y_l)
    
    #for val in p_X_1_X_2_Y_l:
        #debug_print(str(val))                
    

    #step 2: added first attribute name to the new list
    new_v_l.append(attribute_names[0])
    
    #step 3: find max edges for v in new_v_l that are not on the other end of edge in old_v_l
    for item in range(0,len(attribute_names) - 2):
        edges = {}
        max_edge = []
        for v_1 in new_v_l:
            for v_2 in old_v_l:
                if v_1 != v_2 and v_2 not in new_v_l and v_1 != class_values.keys()[0] and v_2 != class_values.keys()[0]: 
                    v_1_index = attribute_names.index(v_1)
                    v_2_index = attribute_names.index(v_2)
                    edges[(v_1,v_2)] = p_X_1_X_2_Y_l[v_1_index][v_2_index]
            
        max_edge = max(edges.iteritems(), key=operator.itemgetter(1))[0]
        max_edge_value = max(edges.iteritems(), key=operator.itemgetter(1))[1]
            
        new_v_l.append(max_edge[1])
        #debug_print(str(attribute_names.index(max_edge[0])) + "," + str(attribute_names.index(max_edge[1])) +" = " + str(max_edge_value))
        max_span_tree_no[(attribute_names.index(max_edge[0]), attribute_names.index(max_edge[1]))] = max_edge_value
        max_span_tree_name[max_edge[0], max_edge[1]] = max_edge_value
        
    
    #debug_print(str(new_v_l))
    #debug_print(str(max_span_tree_no))
    #debug_print(str(max_span_tree_name))
    
    
    #step 4: build parent child set
    parent_child = {}
    
    parent_child[0] = [-1]
    
    #for i in range(0, len(attribute_names) - 1):
    for edge in max_span_tree_no:
        parent_child[edge[1]] = [edge[0]]
    
    #for key in parent_child:
        #debug_print(str(key) + " : " + str(parent_child[key]))
        
        
    #step 5: classfier using naivebayes
    correct = 0
    for name in attribute_names:
        if name != class_values.keys()[0]:
            tempstr = ""
            temp_l = []
            for parent in parent_child[attribute_names.index(name)]:
                if parent != -1:
                    temp_l.append(attribute_names[parent])
            tempstr = " ".join(temp_l)
            debug_print(str(name) + " " +str(tempstr) + " class") 
       
    debug_print("")    

    (p_y_1, p_y_2) = find_prob_class(train_set_data) 
        
    for inst in test_set_data:
        p_xs_y_1 = []
        p_xs_y_2 = [] 
        p_x_y_1 = 1
        p_x_y_2 = 1        
        #debug_print(str(inst))
        for attri in inst:
            #debug_print(str(attri))
            if attri != class_values.keys()[0]:
                parent_key = attribute_names.index(attri)
                p_X_y_1, p_X_y_2 = find_prob_naive_tan(inst, attri, parent_child[parent_key])
                p_xs_y_1.append(p_X_y_1)
                p_xs_y_2.append(p_X_y_2)
         
        for item in p_xs_y_1:
            p_x_y_1 = float(p_x_y_1) * float(item)
            
        for item in p_xs_y_2:
            p_x_y_2 = float(p_x_y_2) * float(item)        
        
   

        p_y_1_x = (float(p_x_y_1) * float(p_y_1)) / ((float(p_x_y_1) * float(p_y_1)) + (float(p_x_y_2) * float(p_y_2)))
        p_y_2_x = float(1) - float(p_y_1_x)

       
        if p_y_1_x > p_y_2_x:
            debug_print(str(attribute_values[class_values.keys()[0]][0]) + " " + str(inst[class_values.keys()[0]]) + " " + str('{0:.16f}'.format(p_y_1_x)))
            if  str(attribute_values[class_values.keys()[0]][0]) == str(inst[class_values.keys()[0]]):
                correct = correct + 1            
        else:
            debug_print(str(attribute_values[class_values.keys()[0]][1]) + " " + str(inst[class_values.keys()[0]]) + " " + str('{0:.16f}'.format(p_y_2_x)))
            if  str(attribute_values[class_values.keys()[0]][1]) == str(inst[class_values.keys()[0]]):
                correct = correct + 1            
        
        
      
    debug_print("")     
    debug_print(str(correct))    
        
    
            
    return 


def predict():
    global test_set_data
    
    if(nort == "n"):
        naivebayes()

    elif(nort == "t"):
        tan()
        
    else:
        naivebayes()


def calculate_output(training_instance):
    
    return output

def main():
    start_jvm()
    get_input()
    populate_data()
    predict()  
    stop_jvm()
    return 0

if __name__ == "__main__":
    main()