#find first 1 in array with 0s and 1s sorted
#idea
#****
#use binary search

def find_first_1(array):
    low = 0
    high = len(array) - 1

    if array[low] == 1:
            return 0    
    
    while low <= high:
        mid = (low + high) / 2
        if array[mid] == 1 and array[mid - 1] == 1:
            high = mid - 1
        elif array[mid] == 0:
            low = mid + 1
        else:
            return mid
     
    return None

if __name__ == "__main__":
    print find_first_1([0,0,1,1,1])
