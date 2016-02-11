#build minimal bst
#set root = mid of array
#and resurse 

from tree import *
from ll import *

def build_min_bst(array, start, end):
    if start > end:
        return None
    
    
    mid = (start + end) / 2
    
    root = node(array[mid])
    root.left = build_min_bst(array, start, mid-1)
    root.right = build_min_bst(array, mid+1, end)
    
    return root

if __name__ == "__main__":
    array = [1,2,3,4,5]
    root = build_min_bst(array, 0, len(array)-1)
    
    tree_bst = tree()
    
    tree_bst.root = root
    #tree_bst.display_nodes()
    
    tree_bst.inorder_traversal(tree_bst.root)
    print tree_bst.tree_data_inorder
    
    tree_bst.preorder_traversal(tree_bst.root)
    print tree_bst.tree_data_preorder


    tree_bst.postorder_traversal(tree_bst.root)
    print tree_bst.tree_data_postorder       