#subtree
#simple one is do inorder and preorder for both trees
#if t2's both inoder and preorder traversals are substring of t1's inorder and preorder traversals respectivelt
#then t2 is a subtree of t1
#edge case is t1 is 3(root)-3(left) t2 is 3(root)-3(right) but the above logic will say t2 is a subtree of t1 which is not right
#so to avoid this, add child nodes with null as data for each child
#O(n+m) memory and O(n+m) time

#or the below one is alternative one


def is_sub_tree(root_1, root_2):
    if root_1 == None:
        return False
    
    if root_1.data == root_2.data:
        if match_tree(root_1, root_2):
            return True
        
    return is_sub_tree(root_1.left, root_2) or is_sub_tree(root_1.right, root_2)

def match_tree(root_1, root_2):
    if root_1 == None and root_2 == None:
        return True
    
    if root_1 == None or root_2 == None:
        return False
    
    if root_1.data != root_2.data:
        return False
    
    return match_tree(root_1.left, root_2.left) and match_tree(root_1.right, root_2.right)



