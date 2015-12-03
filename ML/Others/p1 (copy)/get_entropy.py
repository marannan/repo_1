import sys
import math
from collections import Counter
from globals import *

def calculate_entropy(num, den):
    if (num == 0 or den == 0): return 0
    frac = (float(num))/den
    return frac * (math.log(frac, 2))

def get_class_entropy(data, class_labels):
    class_attributes_values = []
    for element in data:
        if element['class'] == 'positive' or element['class'] == 'negative':
            class_attributes_values.append(element['class'])

    # print attributes_values
    # print len(attributes_values)

    class_entropy = 0
    for label in class_labels:
        class_lable_count = class_attributes_values.count(label)
        probability = float(class_lable_count)/len(class_attributes_values)
        log_probility = math.log(probability, 2)
        class_entropy = class_entropy + probability * log_probility

    return -1 * class_entropy

def get_attribute_entropy(data, attributes_list, attribute, class_label):
    entropy = 0
    for label in attributes_list[attribute]:
        attribute_col = [row[attribute] for row in data]
        label_count = attribute_col.count(label)

        entropy_total = 0
        for class_value in class_label:
            sub_count = sum(1 for row in data if (row[attribute] == label and (row['class'] == class_value)))
            entropy_total = entropy_total + calculate_entropy(sub_count, label_count)
        entropy_total = -1 * entropy_total

        entropy = entropy + float(label_count)/len(data) * (entropy_total)
    return entropy

def calculate_entropy(value_1, value_2):
    if (value_1 == 0 or value_2 == 0):
        return 0
    probability = (float(value_1))/value_2
    entropy = probability * math.log(probability,2)
    return entropy
