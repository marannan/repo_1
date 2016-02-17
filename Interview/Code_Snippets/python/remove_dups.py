hash_table = {}

def to_string(list):
    return "".join(list)

def check_hash_table(item):
    if item in hash_table.keys():
        return True
    else:
        hash_table[item] = True
        return False
    
    
def remove_dup(array):
    
    if len(array) <= 1:
        return array
    
    
    for i in range(len(array)):
        if check_hash_table(array[i]) == True:
            del array[i]
        
            
      
    return array

#sort
#start from 1
#initialise read_ptr and write_ptr to 1
#if element at read_ptr is not equal to read_ptr - 1
#write that element at write+ptr
#move both
#else only mode read_ptr

def remove_dup_2(A):
    n = len(A)
    if(n < 2):
        return n;
    write_ptr = 1
    
    
    
    for read_ptr in range(1, n):
        if(A[read_ptr] != A[read_ptr-1]):
            A[write_ptr] = A[read_ptr];
            write_ptr = write_ptr + 1
        
    return A[:write_ptr];
    
 
if __name__ == "__main__":
    #print remove_dup([1,2,4,4])
    #sort it 
    print remove_dup_2([1,2,2,4,4,3,3])
    #print remove_dup(list("ashokk"))
    #print to_string(set(list("ashokk")))
            
        