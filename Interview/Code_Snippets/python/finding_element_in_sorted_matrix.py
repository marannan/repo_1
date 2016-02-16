#find element in sorted n x m matrix. each row and each column are sorted in ascending order

#idea 
#find elememt x
#if x > start or a row then x should be in rows above the current row because rows below them has to start with more than start of this row
#if x < end of a row then x should be in rows belows current row simply because it cant be above because max of this row is < x so rows above will also be < x
#if x > start or a column then x should be in columns left the current column because clumns right them has to start with more than start of this column
#if x < end of a column then x should be in columns right current column simply because it cant be above because max of this column is < x so columns left will also be < x


#simplification
#x > start of a row then move above
#x < end of row the move below
#x > start of a column then move left
#x < end of a column then move right

def find_in_sorted_matrix(matrix, element):
    if len(matrix) == 0:
        return False
    
    else:
        #initialise row to start of matrix and column to end of first row so narrow down the search
        #starting at start of last column
        row = 0
        column = len(matrix[0]) - 1
        
        while row < len(matrix) and column >=0:
            if matrix[row][column] == element:
                return True, [row,column]
            
            elif matrix[row][column] > element:
                column = column - 1
                
            else:
                row = row + 1
            
