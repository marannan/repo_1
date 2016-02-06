import os
import sys
import collections

hash_table = collections.OrderedDict()

def add_to_hash(i):
    if hash_table.has_key(i) == True:
        hash_table[i] = hash_table[i] + 1
    else:
        hash_table[i] = 1
        #return False
        
    
def find_first_non_repeating(array):
    element_found = False
    
    
    for i in array:
        add_to_hash(i)

    
    for key, val in hash_table.items():
        if val == 1:
            return key
    else:
        return "none"

if __name__ == "__main__":
    
    array = [10,10,2,2]
    print array
    print find_first_non_repeating(array)
    
    