#matrix rotation 90
#to rotate a n x n matrix
#left -> top
#top -> right
#right -> bottom
#bottom -> left
#repeat with all layers of the matrix
#O(n^2)

def matrix_rotate(matrix):
    
    if len(matrix) == 0:
        return matrix
    
    if len(matrix) != len(matrix[0]):
        return "matrix should be n x n"
        #you can do the rotation by padding dummy entries to make it n x n and roatate and remove dummies later
    
    n = len(matrix)
    
    #repeat for all layers
    for layer in range(0, n/2):
        first_index = layer
        last_index = n - 1 - first_index
        
        for i in range(first_index, last_index):
            #how much you want to move to put the elements as part of rotation
            offset = i - first_index
            
            #save the top 
            top  = matrix[first_index][i]
            
            #left -> top
            matrix[first_index][i] = matrix[last_index - offset][first_index]
            
            #bottom -> left
            matrix[last_index - offset][first_index] = matrix[last_index][last_index - offset]
            
            #right -> bottom
            matrix[last_index][last_index - offset] = matrix[i][last_index]
            
            #top -> right
            matrix[i][last_index] = top
            
    
    return matrix


if __name__ == "__main__":
    print matrix_rotate([[1,2],[3,4]])