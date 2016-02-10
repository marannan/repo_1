#tree is balanced
#heights of two subtrees should be <= 1


#return -1 if unbalanced else positive value
from tree import *
def is_tree_balanced(root):
    if root == None:
        return 0
    
    left_height = is_tree_balanced(root.left)
    if left_height == -1:
        return -1
    
    right_height = is_tree_balanced(root.right)
    if right_height == -1:
        return -1
    
    if abs(left_height - right_height) > 1:
        return -1
    
    else:
        return max(left_height, right_height) + 1
    
    
if __name__ == "__main__":
    new_tree = tree(5)
    new_tree.add_node(new_tree.root, "left" ,4)
    new_tree.add_node(new_tree.root, "right", 6)
    new_tree.add_node(new_tree.root.left, "left" ,3)
    new_tree.add_node(new_tree.root.left.left, "left" ,2)
    
    new_tree.display_nodes()
    print new_tree.tree_height()
    
    if is_tree_balanced(new_tree.root) < 0:
        print False
    
    else:
        print True
        
    