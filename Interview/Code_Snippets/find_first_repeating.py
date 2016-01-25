import os
import sys

hash_table = {}

def is_in_hash(i):
    if hash_table.has_key(i) == True:
        return True
    else:
        hash_table[i] = True
        return False
        
    
def find_first_repeating(array):
    element_found = False
    
    for i in reversed(array):
        if is_in_hash(i) == True:
            element_found = True
            position = array.index(i)
        
    
    if element_found == True:
        return array[position]
    else:
        return "none"

if __name__ == "__main__":
    
    array = [1,2,3,4]
    print array
    print find_first_repeating(array)
    
    