#is bst
#do inorder(left,root,right) traversal and it should be sorted array of elements 
#left cannot be > root and right cannot be <= to root


from tree import *
from ll import *
from random import randint


def is_bst(root, min = None, max = None):

    if root == None:
        return True
    
    #when checking a left it cannot be greater than max (root) (it can be equal)
    #when checking a right it cannot be less than min (root)
    if (max != None and root.data > max) or (min != None and root.data <= min):
        return False
    
    if is_bst(root.left, min, root.data) == False or is_bst(root.right, root.data, max) == False:
        return False
    
    
    return True

if __name__ == "__main__":
    tree_bst = tree()
    
    for i in range(0,5):
        tree_bst.add_node_bst(tree_bst.root, randint(0,9))
        
    tree_bst.display_nodes()
    
    print is_bst(tree_bst.root)
    
    tree_bt = tree(5) 
    tree_bt.add_node(tree_bt.root, "left", 5)
    tree_bt.add_node(tree_bt.root, "right", 2)
    tree_bt.add_node(tree_bt.root.left, "left", 3)
    
    tree_bt.display_nodes() 
    
    print is_bst(tree_bt.root)