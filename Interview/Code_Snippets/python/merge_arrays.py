#merge two arrays in sorted order
#array_a is big enough to hold both arrays
#idea
#****
#start from last of two arrays and compare elements and insert at last of array_a

def merge_arrays(array_a, array_b, len_a, len_b):
    
    last_a = len_a - 1
    last_b = len_b - 1
    
    last_ab = len_a + len_b - 1
    last_ab_saved = last_ab
    
    while last_b >=0:
        if last_a >=0 and array_a[last_a] > array_b[last_b]:
            array_a[last_ab] = array_a[last_a]
            last_a = last_a - 1
        
        else:
            array_a[last_ab] = array_b[last_b]
            last_b = last_b - 1            
            
        last_ab = last_ab - 1
        
    
    return array_a[:last_ab_saved + 1]

if __name__ == "__main__":
    print merge_arrays([1,2,3,4,5,0,0,0,0,0,0], [0,1,3], 5, 3)
            