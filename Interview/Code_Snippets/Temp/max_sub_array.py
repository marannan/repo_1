
def max_continuous_sub_arrary(array):
    
    if len(array) == 0:
        return None
    
    if len(array) == 1:
        return array[0]
    
    max_now = array[0]
    max_total = array[0]
    
    for i in range(1,len(array)):
        max_now = max(array[i], max_now + array[i])
        
        max_total = max(max_now, max_total)     
    
            
    return max_total


if __name__ == "__main__":
    print max_continuous_sub_arrary([2,-1,2])
        