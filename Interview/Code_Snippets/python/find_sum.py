import sys
import os

hash_table = {}

def get_from_hash_table(value_1, value_2):

    try:
        if hash_table[value_2] == True:
            return True
    
    except:
        hash_table[value_1] = True
    
    return False


def find_sum(array, sum):
    sum_pairs = []
    if len(array) == 0:
        return False
    
    else:
        for element in array:
            if get_from_hash_table(element, sum - element) == True:
                sum_pairs.append([element,sum-element])
                
            
            
    return sum_pairs
    


def main():
    array = [2,1,9,4,4,56,5,90,3]
    
    sum_pairs = find_sum(array,8)
    if len(sum_pairs) > 0:
        print "yes"
        print sum_pairs
    
    else:
        print "no"
    
    return


if __name__ == "__main__":
    main()