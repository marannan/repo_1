#Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. If there are multiple such triplets, then print any one of them.

#idea
#****
#1) Create an auxiliary array smaller[0..n-1]. smaller[i] should store the index of a number which is smaller than arr[i] and is on left side of arr[i]. smaller[i] should contain -1 if there is no such element.
#2) Create another auxiliary array greater[0..n-1]. greater[i] should store the index of a number which is greater than arr[i] and is on right side of arr[i]. greater[i] should contain -1 if there is no such element.
#3) Finally traverse both smaller[] and greater[] and find the index i for which both smaller[i] and greater[i] are not -1.


def find_3_elements(arr):
    n = len(arr)
    max = n-1 # Index of maximum element from right side
    min = 0 # Index of minimum element from left side
 
    # Create an array that will store index of a smaller
    # element on left side. If there is no smaller element
    # on left side, then smaller[i] will be -1.
    smaller = [0]*10000
    smaller[0] = -1
    for i in range(1,n):
        if (arr[i] <= arr[min]):
            min = i
            smaller[i] = -1
        else:
            smaller[i] = min
 
    # Create another array that will store index of a
    # greater element on right side. If there is no greater
    # element on right side, then greater[i] will be -1.
    greater = [0]*10000
    greater[n-1] = -1
 
    for i in range(n-2,-1,-1):
        if (arr[i] >= arr[max]):
            max = i
            greater[i] = -1
 
        else:
            greater[i] = max
 
    # Now find a number which has both a greater number on
    # right side and smaller number on left side
    for i in range(0,n):
        if smaller[i] != -1 and greater[i] != -1:
            return arr[smaller[i]], arr[i], arr[greater[i]]
        
 
    # If we reach here, then there are no such 3 numbers
    return None