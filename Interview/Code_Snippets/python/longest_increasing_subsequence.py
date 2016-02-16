# Dynamic programming Python implementation of Longest Increasing Subsequence problem

#Let arr[0..n-1] be the input array 
#L(i) be the length of the LIS till index i such that arr[i] is part of LIS and arr[i] is the last element in LIS
#L(i) can be recursively written as.
#L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
#To get LIS of a given array, we need to return max(L(i)) where 0 < i < n

# lis returns length of the longest increasing subsequence
# in arr of size n
def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1 :
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum , lis[i])

    return maximum
# end of lis function

