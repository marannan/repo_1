#using binary search
def sqrt(x):
    if (x == 0):
        return 0
    
    start = 1
    end = x
    
    while (start < end):
        mid = start + (end - start) / 2
        #Look for the critical point: i*i <= x && (i+1)(i+1) > x
        if (mid <= x / mid and (mid + 1) > x / (mid + 1)): #Found the result
            return mid
        elif (mid > x / mid): # Keep checking the left part
            end = mid
        else:
            start = mid + 1 # Keep checking the right part
    
    return start;


if __name__ == "__main__":
    print sqrt(10)