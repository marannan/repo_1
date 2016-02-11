#find path in a tree

#add node data to path
#check at each node if this node completes the path to the given sum
#resurse with left and right 


def find_sum_path(root, sum, path, level=0):
    if root == None:
        return 
    
    path[level] = root.data
    
    t_sum = 0
    
    for i in range(level,-1,-1):
        t_sum = t_sum + path[i]
        if t_sum == sum:
            print path[i:level]
            
    find_sum_path(root.right, sum, path, level + 1)
    find_sum_path(root.left, sum, path, level + 1)
    
    #removing the unwanted node
    path.pop(level)