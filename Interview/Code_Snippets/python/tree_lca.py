#least common ancestor of x and y
#perform inoder traversal
#perform postorder traversal
#get list of elements from inorder traversal between x and y
#out of the elements, element at the highest index in post order traversal is the lca of x and y

from tree import *
from ll import *


def find_lca(root, node_x, node_y):
    if root == None:
        return None
    
    if node_x == None or node_y.right == node_x or node_y.right == node_x:
        return node_y
    
    if node_y == None or node_x.right == node_y or node_x.right == node_y:
        return node_x    
    
    tree_bt = tree()
    tree_bt.root = root
    
    inorder_list = tree_bt.inorder_traversal(tree_bt.root)
    postorder_list = tree_bt.postorder_traversal(tree_bt.root)
    
    for nodes in inorder_list:
        if node > x and node < y:
            ancestors.append(node)
        
    lca = None   
    for ancestor in ancestors:
        if lca != None and postorder_list.getindex(ancestor) > lca:
            lca = postorder_list.getindex(ancestor)
            
    return lca
    
    
