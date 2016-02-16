#for stream of integers
#write fns to add the new no and get rank (no of elements <= given no)

#we can use arrays and insert new no in ascending order and rank would be its index
#but insertion is inefficient as it'd require shifing elements

#use bst
#store no of elements in left tree in each node
#inorder traversal to get rank
#use counter and to get rank and counter increases we move to right and doesnt when we move to left(decreasing order)

#full solution in ctci book pg 375         

def get_rank(root, x):
    if root == None:
        return -1
    
    if root.data == x:
        return root.left_tree_size()
    
    #right side increament counter
    if x > root.data:
        return root.left_tree_size + 1 + get_rank(root.right, x)
    
    #;eft side dont increment counter
    if x < root.data:
        return get_rank(root.left, x)
    
