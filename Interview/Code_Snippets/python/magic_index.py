#find magic index in an array
#magic index is array[magic_index] = magic_index

#if unsorted use brute force to check all elements one by one O(n)
#if sorted, use binary search 

def find_magic_index(array, start, end):
    if start > end or start < 0 or end >= len(array):
        return -1
    
    mid = (start + end) / 2
    if array[mid] == mid:
        return mid
    
    #search left
    #we dont have to search the entire left. so left search limit is calculated below
    left_end = min(array[mid], mid - 1)
    left = find_magic_index(array, start, left_end)
    
    if left >= 0:
        return left
    
    #search right
    right_start = max(mid + 1, array[mid])
    right = find_magic_index(array, right_start, end)
    
    return right

if __name__ == "__main__":
    print find_magic_index([-10,-5,2,2,2,3,4,7,9,12,13], 0, len([-10,-5,2,2,2,3,4,7,9,12,13])-1)