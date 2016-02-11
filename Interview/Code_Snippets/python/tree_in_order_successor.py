#inorde successor (left, root, right)

#if node has right branch then left most child of the right breach is its inorder successor
#else move up until n is the left child for its parent
#return n


def find_inorder_successor(node):
    if node == None:
        return None
    
    if node.right != None:
        return find_left_most_child(node.right)
    
    parent = node.parent
    
    while node != None and parent.right == node:
        node = node.parent
        parent = node.parent

    return parent

def find_left_most_child(node):
    if node == None:
        return None
    
    while node.left:
        node = node.left
        
    return node

