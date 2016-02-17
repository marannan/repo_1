#find smallest missing element in an array

#idea
#****
#1) Segregate positive numbers from others i.e., move all non-positive numbers to left side. Ignore them. 
#2) We traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of value at index x to negative
#3) We traverse the array again and print the first index which has positive value


#if array has 1 then 0th element will be changed to -ve and so on so iterate for first pass to make array negative
#second pass to find first positive element and return index + 1
#if element is present our first pass would have made arrat[element - 1] as -ve 

#algo
#starting from index 0 we make the element pointed by index = abs(array[i]) - 1 as negative value (1 is subtracted because index start from 0 and positive numbers start from 1)
#now traverse and if you find a positive stop which means the index pointing to this element is not present
#return index + 1 (1 is added becuase indexes start from 0)

#other solution
#We can also use hashing. We can build a hash table of all positive elements in the given array. 
#Once the hash table is built. We can look in the hash table for all positive integers, starting from 1. 
#As soon as we find a number which is not there in hash table, we return it. 
#This approach may take O(n) time on average, but it requires O(n) extra space.

#other solution
#If the datastructure can be mutated in place and supports random access 
#then you can do it in O(N) time and O(1) additional space. 
#Just go through the array sequentially and for every index write the value at the index to the index specified by value, 
#recursively placing any value at that location to its place and throwing away values > N. Then go again through the array looking for the spot where value doesn't match the index - that's the smallest value not in the array. 
#This results in at most 3N comparisons and only uses a few values worth of temporary space.

def find_missing_2(array):
    N = len(array)
    # Pass 1, move every value to the position of its value
    for cursor in range(N):
        target = array[cursor]
        while target < N and target != array[target]:
            new_target = array[target]
            array[target] = target
            target = new_target
    
    # Pass 2, find first location where the index doesn't match the value
    for cursor in range(N):
        if array[cursor] != cursor:
            return cursor
    return N

#1st solution
def find_missing(array):

    #first pass    
    for i in range(len(array)):
    
        #check to make sure we dont point outside or point to non positive
        if abs(array[i]) - 1  < len(array) and array[abs(array[i]) - 1] > 0: 
            #make that element negative
            array[abs(array[i]) -1] = - array[abs(array[i]) - 1];

    #if array has 1 then 0th element will be changed to -ve and so on
    #second pass to find first positive element and return index + 1
    for i in range(len(array)):
        if array[i] > 0:
            return i + 1

    #return last element + 1
    return array[len(array)-1] + 1


if __name__ == "__main__":
    from push_pos_last import *
    array = push_pos_last([ 1, 10, 2])
    print find_missing(array)