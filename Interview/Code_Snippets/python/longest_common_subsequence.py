#Dynamic Programming implementation of LCS problem

#idea
#****

#Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n respectively. 
#And let L(X[0..m-1], Y[0..n-1]) be the length of LCS of the two sequences X and Y. 
#Following is the recursive definition of L(X[0..m-1], Y[0..n-1]).

#If last characters of both sequences match (or X[m-1] == Y[n-1]) then
#L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

#If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
#L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2])

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
                
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
                
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs

if __name__ == "__main__":
    print lcs("ABCDGH", "AEDFHR")