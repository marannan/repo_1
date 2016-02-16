#return all repeating elements in an array

#idea
#****
#traverse the list for i= 0 to n-1 elements
#{
    #check for sign of A[abs(A[i])] ;
    #if positive then
    #make it negative by   A[abs(A[i])]=-A[abs(A[i])];
    #else  // i.e., A[abs(A[i])] is negative
    #this   element (ith element of list) is a repetition
#}

#we make the element pointed by index  = abs(array[i]) as negative value
#so if there are same two elements so both taken as index will point to the same element 
#so during first occurance it'll change the element pointed as negative 
#during second occurance if the elemented pointed is already is negative which means this is a repeatition

def find_repeating(array):

    repeating = []
    
    for i in range(len(array)):
    
        if (array[abs(array[i])] >= 0):
            array[abs(array[i])] = - array[abs(array[i])];
        else:
            repeating.append(abs(array[i]))

    return repeating


if __name__ == "__main__":
    print find_repeating([1, 2, 3, 1, 3, 6, 6])