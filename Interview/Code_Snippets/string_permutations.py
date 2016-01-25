import sys
import os

b = [0,0,0]
c = [0,1]

def swap(a,l,r):
    t = a[l]
    a[l] = a[r]
    a[r] = t
    return a
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a = swap(a,l,i)
            permute(a, l+1, r)
            a = swap(a,l,i) # backtrack
            
            
def perm(n1, n2):
    global c, b
    if n1 <= 0:
        print b
    else:
        for l in c:
            b[n1-1] = l
            perm(n1-1, n2)
        #b[n1-1] = 1
        perm(n1-1, n2)
    
 
if __name__ == "__main__":# Driver program to test the above function
    string = "ABC"
    n = len(string)
    a = list(string)
    permute(a, 0, n-1)

    #perm(3, 3)