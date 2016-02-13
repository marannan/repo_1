#generate all valid combinations of parenthesis

#idea
#****
#create a binary string of length equal to 2*n for n pair of parenthesis
#each bit can be 0 or 1 ie '(' or ')'
#start with index = 0
#set binary_string[index] = ( and other bits can be anything so recurse with index++
#set binary_string[index] = ) and other bits can be anything so recurse with index ++ 
#base condition is index == n add string to list 

#this list will contain invalid parenthesis for example "((((" 
#check the validness and remove invalid ones
#also remove duplicates if any and return the final list


from parenthesis_check import *

bit_array = [] * 1000
paranthesis_map = {0:"(", 1:")"}
string_list = []

def paranthesis_generation_1(n, index = 0):
    
    if index == n:
        string_list.append(bit_array[:n])

    else:
        bit_array[index] = 0
        n_bit_strings(n, index + 1)
        bit_array[index] = 1
        n_bit_strings(n, index + 1)
        
#idea
#****
#left_remaining is no of ( remaining and right_remaining is no of ) remaining will be initialised to n for generating a n pair of parenthesis
#if left_remaining and right_remaining == 0 print that expression #base case
#start at index 0
#you can always insert left as long as we havent used all left parenthesis
#recurse with index++
#insert right as long as the expression is valid. example "())" it'll be invalid if more right than left exists
#resurse with index++


def parenthesis_generation_2(paranthesis_combinations, left_rem, right_rem, paren_exp, index = 0):

    #invalid case
    if left_rem < 0 or right_rem < left_rem:
        return
    
    #base case
    if left_rem == 0 and right_rem == 0:
        paranthesis_combinations.append("".join(paren_exp))
        
    
    else:
        #you can always insert left as long as we havent used all left parenthesis
        if left_rem > 0:
            paren_exp[index] = "("
            parenthesis_generation_2(paranthesis_combinations, left_rem - 1, 
                                    right_rem, 
                                    paren_exp, 
                                    index + 1)
            
        #insert right as long as the expression is valid. example "())" it'll be invalid if more right than left exists
        if right_rem > left_rem:
            paren_exp[index] = ")"
            parenthesis_generation_2(paranthesis_combinations, left_rem, 
                                                right_rem - 1, 
                                                paren_exp, 
                                                index + 1)
            
    return paranthesis_combinations
            

if __name__ == "__main__":

    #for first method
    #global sting_list
    #sting_list = n_bit_strings(2)
    #paranthesis_combinations = []
    #for string in string_list:
        #paranthesis_exp = ""
        #for char in string:
            #paranthesis_exp = paranthesis_exp + paranthesis_map[char]
        #if is_valid_2(paranthesis_exp):
            #paranthesis_combinations.append(paranthesis_exp)
    
    #for parenthesis_exp in set(paranthesis_combinations):
        #print parenthesis_exp
        
        
    
    #for second method
    paranthesis_combinations = []
    n = 3
    paren_exp = [-1] * 2 * n
    
    parenthesis_generation_2(paranthesis_combinations, n, n, 
                            paren_exp)
    
    for parenthesis_exp in set(paranthesis_combinations):
        print parenthesis_exp

    