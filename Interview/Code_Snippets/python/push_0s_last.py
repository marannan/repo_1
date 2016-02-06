import sys
import os


def push_0s_last(array):
    
    i = 0
    j = 0
    
    for i in range(0,len(array)):
        if array[i] != 0:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j = j + 1
    

    return array

if __name__ == "__main__":
    array = [-4,0,-2,5,0,-1,4,3]
    print array
    print push_0s_last(array)