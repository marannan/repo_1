__author__ = 'ashokmarannan'
from globals import *
from operator import le, gt, eq
from get_entropy import calculate_entropy, get_attribute_entropy, get_class_entropy

tab_space = '|\t'

def attribute_no_count(data, attribute, class_label):
    labels_list = []
    values = []

    try:
        minimum_entropy = float('inf')
    except:  # check for a particular exception here?
        minimum_entropy = 1e30000

    minimum_entropy_attribute = ""
    minnum_label = 0

    # for instance in data:
    #     values.append(instance[attribute])

    #values.sort();

    values = sorted(list(set([dict_list[attribute] for dict_list in data])))


    for element in range(len(values)-1):
       labels_list.append((float(values[element])+values[element+1])/2)


    for label in labels_list:
        count_less_than = sum(1 for row in data if row[attribute] <= label)
        count_more_than = len(data) - count_less_than

        entorpy_more_than = 0
        entropy_less_than = 0

        for class_value in class_label:
            subtree_count_less = sum(1 for row in data if (row[attribute] <= label and
                                                   (row['class'] == class_value)))
            entropy_less_than = entropy_less_than + calculate_entropy(subtree_count_less, count_less_than)

            subtree_count_more = sum(1 for row in data if (row[attribute] > label and
                                                   (row['class'] == class_value)))
            entorpy_more_than = entorpy_more_than + calculate_entropy(subtree_count_more, count_more_than)

        entropy_less_than = -1 * entropy_less_than
        entorpy_more_than = -1 * entorpy_more_than

        entropy = (float(count_less_than)/len(data)) * (entropy_less_than) + (float(count_more_than)/len(data))*entorpy_more_than
        if (entropy < minimum_entropy):
            minimum_entropy = entropy
            minnum_label = label

    return (minnum_label, minimum_entropy)


def find_best_candidate_split(data, attributes_list, attributes_label, class_label):
    try:
        minimum_entropy = float('inf')
    except:  # check for a particular exception here?
        minimum_entropy = 1e30000

    minimum_entropy_attribute = ""
    threshold_value = -1

    for attribute in attributes_label:
        if attributes_list.has_key(attribute) == False: #if numeric
            (threshold_value, entropy_value) = attribute_no_count(data, attribute, class_label)

        else:
            entropy_value = get_attribute_entropy(data, attributes_list, attribute, class_label)
        #print "attr: {0} entropy: {1}".format(attribute, entropy_value)

        if entropy_value < minimum_entropy:
            minimum_entropy = entropy_value
            minimum_entropy_attribute = attribute
            if attributes_list.has_key(attribute) == False: #if numeric
                threshold = threshold_value
        #print "minattr: {0} entropy: {1}".format(minimum_entropy_attribute, minimum_entropy)

    #print "minimum attr: {0} minimum entropy: {1} threshold: {2}".format(minimum_entropy_attribute, minimum_entropy, threshold_value)

    return (minimum_entropy, minimum_entropy_attribute, threshold)



def build_decision_tree(data, level, attributes_list, attributes_label, class_label, m=1):

    (minimum_entropy, minimum_entropy_attribute, threshold)= find_best_candidate_split(data, attributes_list, attributes_label, class_label)

    child = decision_tree(minimum_entropy_attribute, threshold, [], attributes_list, attributes_label, class_label)

    if attributes_list.has_key(minimum_entropy_attribute) == False: #if numeric


        leaf_node_reached = False
        count_1 = sum(1 for row in data if row[minimum_entropy_attribute] <= threshold and row['class'] == class_label[0])
        count_2 = sum(1 for row in data if row[minimum_entropy_attribute] <= threshold and row['class'] == class_label[1])
        class_value = class_label[0] if count_1>=count_2 else class_label[1]
        if (count_1 + count_2) < m or count_1 == 0 or count_2 == 0:
            leaf_node_reached = True

        if (leaf_node_reached == True):
            child.addnode(decision_tree(minimum_entropy_attribute, threshold, class_value, attributes_list, attributes_label, class_label))


        if (leaf_node_reached == False):
            sub_train_data = [row for row in data if row[minimum_entropy_attribute] <= threshold]
            child.addnode(build_decision_tree(sub_train_data, level+1, attributes_list, attributes_label, class_label, m))

        leaf_node_reached = False
        count_1 = sum(1 for row in data if row[minimum_entropy_attribute] > threshold and row['class'] == class_label[0])
        count_2 = sum(1 for row in data if row[minimum_entropy_attribute] > threshold and row['class'] == class_label[1])
        class_value = class_label[0] if count_1>=count_2 else class_label[1]
        if (count_1 + count_2) < m or count_1 == 0 or count_2 == 0:
            leaf_node_reached = True


        if (leaf_node_reached == True):
            child.addnode(decision_tree(minimum_entropy_attribute, threshold, class_value, attributes_list, attributes_label, class_label))


        if (leaf_node_reached == False):
            sub_train_data = [row for row in data if row[minimum_entropy_attribute] > threshold]
            child.addnode(build_decision_tree(sub_train_data, level+1, attributes_list, attributes_label, class_label, m))

    else:
        for element in attributes_list[minimum_entropy_attribute]:
            leaf_node_reached = 0
            max_class_count = -1
            max_class_value = -1
            total_class_count = 0

            for class_label_item in class_label:
                count = sum(1 for row in data if row[minimum_entropy_attribute] == element and row['class'] == class_label_item)
                total_class_count = total_class_count +  count
                if count > max_class_count:
                    max_class_count = count
                    max_class_value = class_label_item
                if count == 0:
                    leaf_node_reached = 1

            if (total_class_count < m):
                leaf_node_reached = 1

            if (leaf_node_reached == 1):
                child.addnode(decision_tree(minimum_entropy_attribute, 0, max_class_value, attributes_list, attributes_label, class_label))
                continue
            else:
                sub_train_data = [row for row in data if row[minimum_entropy_attribute] == element]
                child.addnode(build_decision_tree(sub_train_data, level+1, attributes_list, attributes_label, class_label, m))

    return child

class decision_tree(object):
    def __init__(self, attribute_name, threshold, class_or_child, attributes_list, attributes_label, class_label):
        self.attribute_name = attribute_name
        self.threshold = threshold
        self.class_or_child = class_or_child
        self.attributes_list = attributes_list
        self.attributes_label = attributes_label
        self.class_label = class_label

    def addnode(self, child):
        if (isinstance(self.class_or_child, basestring)):
            raise ValueError("Error: node cannot be added")
        else:
            self.class_or_child.append(child)

    def display_tree(self, level):
        temp_str= "".join([tab_space for _ in range(level)]) + self.attribute_name
        return_str = ""
        if self.attributes_list.has_key(self.attribute_name) == False: #if numeric
            return_str = temp_str+ "<=" +str(self.threshold)
            if isinstance(self.class_or_child, basestring):
                print "{1}: {0}".format(self.class_or_child, return_str)
            else:
                print return_str
                self.class_or_child[0].display_tree(level+1)
            return_str = temp_str+ ">" + str(self.threshold)
            if isinstance(self.class_or_child, basestring):
                return_str+= ": {0}".format(self.class_or_child)
                print return_str
            else:
                print return_str
                self.class_or_child[1].display_tree(level+1)
        else:
            if isinstance(self.class_or_child, basestring):
                print temp_str + ": {0}".format(self.class_or_child)
            else:
                for index, child in enumerate(self.class_or_child):
                    print temp_str + "=" + self.attributes_list[self.attribute_name][index]

                    self.class_or_child[index].display_tree(level+1)

    def threshold_check(self, instance):
        if self.attributes_list.has_key(self.attribute_name) == False: #if numeric
            if instance[self.attribute_name] <= self.threshold:
                return 0
            else:
                return 1
        return self.attributes_list[self.attribute_name].index(instance[self.attribute_name])

    def class_predict(self, instance):
        if isinstance(self.class_or_child, basestring):
            return self.class_or_child
        child_index = self.threshold_check(instance)
        return self.class_or_child[child_index].class_predict(instance)