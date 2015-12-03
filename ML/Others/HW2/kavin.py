__author__ = 'kavin'
# coding: utf-8

import sys
import re
import math
from random import shuffle

global correctly_predicted_test
global data_instance_list

attribute_list = []
class_label = []
instance_class_label_list = []
data_instance_list = []
output_list = []
data_found = False
num_positive = 0
num_negative = 0
correctly_predicted_test = 0


folds = 10
bias = 0.1
fold_list = []
weights = []
positive_instance_index = []
negative_instance_index = []
epochs = 1000
learning_rate = 0.1


def sigmoid(value):
    return 1.0 / (1.0 + math.exp(-value))


def compute_net_input(instance):
    sum = 0
    for i in range(0,len(instance)):
        sum = sum + (float(instance[i]) * weights[i])
    return (sum + bias)


def stratify(positive_instance_index, negative_instance_index):
    global folds
    global data_instance_list
    global fold_list

    shuffle(negative_instance_index)
    shuffle(positive_instance_index)

    fold_list = [None]*len(data_instance_list)

    positive_ratio = float(num_positive) / float(num_positive + num_negative)
    negative_ratio = float(num_negative) / float(num_positive + num_negative)

    num_instances_per_fold = float(len(data_instance_list)) / float(folds)

    positive_instances_per_fold = int(positive_ratio * num_instances_per_fold)
    negative_instances_per_fold = int(num_instances_per_fold - positive_instances_per_fold)


    pos_index = 0
    neg_index = 0

    for i in range(0, folds):
        for j in range(0, positive_instances_per_fold):
            if pos_index < len(positive_instance_index):
                fold_list[positive_instance_index[pos_index]] = i
                pos_index = pos_index + 1
        for j in range(0, negative_instances_per_fold):
            if neg_index < len(negative_instance_index):
                fold_list[negative_instance_index[neg_index]] = i
                neg_index = neg_index + 1

    fold_index = 0
    for i in range(pos_index, len(positive_instance_index)):
        fold_list[positive_instance_index[i]] = fold_index
        fold_index = (fold_index + 1)%folds

    for i in range(neg_index, len(negative_instance_index)):
        fold_list[negative_instance_index[i]] = fold_index
        fold_index = (fold_index + 1)%folds



def update_weight_bias(delta, instance_index):
    global attribute_list
    global data_instance_list
    global learning_rate
    global weights
    global bias

    for i in range(0, len(attribute_list)):
            change_in_weight = delta * (learning_rate * float(data_instance_list[instance_index][i]))
            weights[i] = weights[i] + change_in_weight

    bias = bias + delta;


def train_neural_net(test_fold):
    global data_instance_list
    global attribute_list
    global fold_list
    global instance_class_label_list

    correctly_predicted = 0
    total_predicted = 0

    for i in range(0, len(data_instance_list)):
        if fold_list[i] == test_fold:
            continue
        else:
            total_predicted = total_predicted + 1
            predicted_class = ''
            actual_class = instance_class_label_list[i]

            if actual_class.lower() == 'mine':
                actual_output = 1.0
            elif actual_class.lower() == 'rock':
                actual_output = 0.0

            net_weight = compute_net_input(data_instance_list[i])
            output = sigmoid(net_weight)
            if(output > 0.5):
                predicted_class = 'Mine'
            else:
                predicted_class = 'Rock'

            if actual_class.lower() == predicted_class.lower():
                correctly_predicted = correctly_predicted + 1

            delta = (output) * (1 - output) * (actual_output - output);
            update_weight_bias(delta,i);
    return float(correctly_predicted) / float(total_predicted)


def test_neural_net(test_fold):
    global output_list
    global data_instance_list
    global fold_list
    global instance_class_label_list
    global correctly_predicted_test

    num_predicted = 0
    correctly_predicted = 0

    for i in range(0, len(data_instance_list)):
        if fold_list[i] == test_fold:
            num_predicted = num_predicted +1
            actual_class = instance_class_label_list[i]
            predicted_class = ''

            net_weight = compute_net_input(data_instance_list[i])
            output = sigmoid(net_weight)

            if output > 0.5:
                predicted_class = 'Mine'
            else:
                predicted_class = 'Rock'

            if actual_class.lower() == predicted_class.lower():
                correctly_predicted = correctly_predicted + 1
                correctly_predicted_test = correctly_predicted_test + 1

            output_to_print = [test_fold, predicted_class, actual_class, output]

            output_list[i] = output_to_print
    return float(correctly_predicted)/float(num_predicted)


def train_and_test():
    global folds
    global weights
    global attribute_list
    global bias
    global epochs
    global output_list
    global data_instance_list

    output_list = [None] * len(data_instance_list)
    for i in range(0, folds):
        weights = [0.1] * len(attribute_list)
        bias = 0.1

        test_fold = i

        for j in range(0, epochs):
            train_neural_net(test_fold)

        test_neural_net(test_fold)


def print_output():
    global output_list
    global a
    for i in range(0, len(output_list)):
        output = str(output_list[i][0]) + ' ' + output_list[i][1] + ' ' + output_list[i][2] + ' ' + str(output_list[i][3])
        print output

def parse_arff_file(file_path):
    global attribute_list
    global class_label
    global data_instance_list
    global positive_instance_index
    global negative_instance_index
    global data_found
    global num_negative
    global num_positive

    with open(file_path, 'r') as source_file:
        
        for line in source_file:

            attribute_regex = re.compile('@attribute\s+(.*)')
            class_regex = re.compile('@attribute\s+\'Class\'\s+(.*)')

            attribute_name_type = attribute_regex.findall(line)
            #print line
            #print attribute_name_type
            #print len(attribute_name_type)
            name_type_list = []
            if len(attribute_name_type) > 0:
                name_type_list = attribute_name_type[0].split()
            #print name_type_list
            if len(name_type_list) > 0:
                if name_type_list[1] == 'numeric':
                    name_type_list[0].replace('\'','')
                    #print 'Appended attribute : ', name_type_list[0]
                    attribute_list.append(name_type_list[0])
                else:
                    #print name_type_list
                    class_label_found = False
                    for word in name_type_list:
                        if word == '\'Class\'' or word == 'Class':
                            #print 'Class label found'
                            class_label_found = True
                            break;

                    if class_label_found:
                        class_label = []
                        for word in name_type_list:
                            if word == '{':
                                index = name_type_list.index(word)
                                name_type_list.remove(word)
                                #print 'Removed {'

                            elif ',' in word:
                                index = name_type_list.index(word)
                                word = word.replace(',','')
                                #print word
                                #print 'Removed ,'
                                name_type_list[index] = word

                            elif '}' in word:
                                index = name_type_list.index(word)
                                word = word.replace('}','')
                                #print word
                                name_type_list[index] = word
                        #print name_type_list
                        name_type_list[1] = name_type_list[1].replace(',','')
                        class_label.append(name_type_list[1])
                        class_label.append(name_type_list[2])
                        #print class_label

            if '@data' in line:
                data_found = True
                #print data_found

            if data_found:
                if '@data\n' not in line:
                    data_instance = line.split(',')
                    #print data_instance
                    instance = data_instance[0:len(data_instance)-1]
                    instance_class_label = data_instance[len(data_instance)-1].replace('\n','')

                    instance_class_label_list.append(instance_class_label)
                    data_instance_list.append(instance)

                    if instance_class_label == class_label[0]:
                        num_negative = num_negative + 1
                        negative_instance_index.append(data_instance_list.index(instance))
                    elif instance_class_label == class_label[1]:
                        num_positive = num_positive + 1
                        positive_instance_index.append(data_instance_list.index(instance))

def main():
    global epochs
    global folds
    global learning_rate

    program_arguments = sys.argv
    file_path = program_arguments[1]
    folds = int(program_arguments[2])
    learning_rate = float(program_arguments[3])
    epochs = int(program_arguments[4])

    parse_arff_file(file_path)
    stratify(positive_instance_index, negative_instance_index)
    train_and_test()
    print_output()
    test_accuracy = float(correctly_predicted_test)/float(len(data_instance_list))
    print test_accuracy

if __name__ == "__main__":
    main()