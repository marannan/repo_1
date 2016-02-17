#Returns length of the longest contiguous subsequence
#idea
#****
#1) Create an empty hash.
#2) Insert all array elements to hash.
#3) Do following for every element arr[i]
#....a) Check if this element is the starting point of a 
            #subsequence.  To check this, we simply look for
            #arr[i] - 1 in hash, if not found, then this is
            #the first element a subsequence.  

            #If this element is a first element, then count 
            #number of elements in the consecutive starting 
            #with this element.

            #If count is more than current res, then update    
            #res.
            
def findLongestConseqSubseq(array):

    hash_table = {}
    ans = 0;
 
    #Hash all the array elements
    for i in range(len(array)):
        hash_table[i] = array[i]
 
    #check each possible sequence from the start
    #then update optimal length
    for i in range(len(array)):

        #if current element is the starting
        #element of a sequence
        if (array[i] - 1) in hash_table.values():
        
            #Then check for next elements in the sequence
            j = array[i];
            while j in hash_table.values():
                j = j + 1
 
            #update  optimal length if this length is more
            ans = max(ans, j - arr[i])

    return ans;
