#Returns count of possible paths to reach cell at row number m and column from top left
#number n from the topmost leftmost cell (cell at 1, 1)
#O(mn).

def no_paths(m,n):
    
    #Create a 2D table to store results of subproblems       
    count = [[0 for x in range(m)] for x in range(n)]
 
    #Count of paths to reach any cell in first row is 1
    for i in range(m):
        count[i][0] = 1
 
    #Count of paths to reach any cell in first column is 1
    for j in range(n):
        count[0][j] = 1
        
    ##some cells are marked non steppable 
    #count[1][2] = None
 
    #Calculate count of paths for other cells in bottom-up manner using
    #the recursive solution
    for i in range(1,m):
        for j in range(1,n):

            #skip non steppable cells
            if count[i][j] == None:
                count[i][j] = 0
                continue
            
            #By uncommenting the last part the code calculatest the total possible paths if the diagonal Movements are allowed
            count[i][j] = count[i-1][j] + count[i][j-1] #+ count[i-1][j-1]
 
    
    return count[m-1][n-1];


if __name__ == "__main__":
    print no_paths(3,3)