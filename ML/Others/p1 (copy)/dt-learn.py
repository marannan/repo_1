import sys
import os
from globals import *
from operator import le, gt, eq
from get_data import get_data, get_attribute_value, get_attributes_label
from get_entropy import get_class_entropy
from decision_tree import decision_tree, build_decision_tree

def populate_data():
    global train_set_data, test_set_data, attributes_list, attributes_label, class_label
    train_set_data = get_data(train_set_file);
    test_set_data = get_data(test_set_file);
    attributes_list = get_attribute_value(train_set_file)
    attributes_label = get_attributes_label(train_set_file);
    class_label = attributes_list['class']

    # print train_set_data
    # print attributes_list
    # print attributes_label
    # print class_label

def get_input():
    global train_set_file
    global test_set_file
    global m
    train_set_file = sys.argv[1]
    test_set_file = sys.argv[2]
    m = int(sys.argv[3])
    if(os.path.isfile(train_set_file) == False):
        print "Error: train set %s cannot be opened",(train_set_file)
        sys.exit(0)
    if(os.path.isfile(test_set_file) == False):
        print "Error: test set %s cannot be opened",(test_set_file)
        sys.exit(0)
    try:
        m = int(sys.argv[3])
    except ValueError:
        print("Error: m is not an int!")
        sys.exit(0)

    # print "training set = " + train_set_file
    # print "testing set = " + test_set_file
    # print "m = " + str(m)

    return 0

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


def main():
    #global train_set_data, test_set_data, attributes_lables, attributes_nom_values,
    #global class_labels
    get_input()
    populate_data()
    class_entroy = get_class_entropy(train_set_data, class_label)
    #print class_entroy
    root = build_decision_tree(train_set_data, 0, attributes_list, attributes_label, class_label, m)
    root.display_tree(0)
    predict_test_data(root)
    return 0

if __name__ == "__main__":
    main()