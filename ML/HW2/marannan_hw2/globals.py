__author__ = 'ashokmarannan'
import sys

#globals
data_set_file = "nofile"
test_set_file = "nofile"
data_set = {}
attributes_list = {}
attributes_label = []
class_label = []
class_entropy = 0
n = 10
l = 0.1
e = 1
root = 0
no_pos = 0
no_neg = 0
no_inst_per_fold = 0 
positive_set = []
negative_set = []
data_folds = []
pos_ratio = 0
neg_ratio = 0
firstclass =0
secclass = 0


