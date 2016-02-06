import sys
import os


def rearrange(array):
    if len(array) == 0 or len(array) == 1:
        return array
    
    i = 0
    j = 0
    
    for i in range(0, len(array)):
        if array[i] <= 0:
            temp = array[i]
            i_old = i
            while i > j:
                array[i] = array[i-1]
                i = i - 1
            array[j] = temp
            j = j + 1
            i = i_old
            #print array

        
      
    #print array
    
    neg = 1
    pos = j
   
    while pos < len(array) and neg < len(array) and array[neg] < 0:
        temp = array[pos]
        pos_old = pos
        while pos > neg:
            array[pos] = array[pos - 1]
            pos = pos - 1
        array[neg] = temp
        pos = pos_old
        pos = pos + 1
        neg = neg + 2
        #print array
       

    return array    
    
    

if __name__ == "__main__":
    array = [4,1,-1,-2,3,-6]
    print array
    print rearrange(array)