
alphabet = ["", "a", "b", "c", "d", "e",
            "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "v", "z"]

class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

#build a tree with root as array and left child as first digit of array and right as first two digits recursively
#print all leaves 

#http://www.geeksforgeeks.org/find-all-possible-interpretations/


def print_words(digit, string, array):

    if digit > 26:
        return None
    
    data = str(string + alphabet[digit])
    
    new_node = node(data)
    
    if len(array) != 0:
        digit = array[0]
        new_node.left = print_words(digit, data , array[1:])
        
        if len(array) > 1:
            digit = array[0] * 10 + array[1]
            new_node.right = print_words(digit, data, array[2:])
            
    
    return new_node

def print_tree_leaves(root):
    if root == None:
        return
    
    if root.left == None and root.right == None:
        print root.data
        
    print_tree_leaves(root.left)
    print_tree_leaves(root.right)
    

if __name__ == "__main__":
    root = print_words(0, "", [1,1])
    print_tree_leaves(root)

