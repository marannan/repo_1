def first_last(array):
    if len(array) <= 2:
        return array
    
    start = 1;
    end = len(array) - 1
    
    while start < end:
        temp = array[end]
        for i in range(end, start, -1):
            array[i] = array[i-1]
        array[start] = temp
        
        start += 2
        
    
    return array

if __name__ == "__main__":
    print first_last([1,2,3,4,5,6])
    
        