
def matrix_zeros(matrix):
    if len(matrix) == 0:
        return matrix
    
    row = [False] * len(matrix)
    column = [False] * len(matrix[0]) 
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #print matrix[i][j]
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True
                
    
    for i in range(len(row)):
        if row[i] == True:
            matrix[i] = [0]*len(matrix[0])
            #new_matrix = make_row_zero(matrix,i)
            
            
    for i in range(len(column)):
        if column[i] == True:
            matrix = make_column_zero(matrix,i)
            
    
    return matrix

def make_row_zero(matrix, row_no):
    
    for i in range(len(matrix[0])):
        matrix[row_no][i] = 0
    
    return matrix

def make_column_zero(matrix, column_no):
    
    for i in range(len(matrix)):
        matrix[i][column_no] = 0
        
    return matrix
    

if __name__ == "__main__":
    
    matrix_zero =  matrix_zeros([[1,0,2],[3,4,0],[5,6,7]])
    for row in matrix_zero:
        print row
    