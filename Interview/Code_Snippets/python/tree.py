#tree
from random import randint

class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
        
    
class tree:
    def __init__(self,data = None):
        self.root = node(data)
        self.tree_data_inorder = []
        self.tree_data_preorder = []
        self.tree_data_postorder = []
        self.node_added = False
        
    
    def add_node_bst(self, root, data):
        child = node(data)
        
        if node == None:
            self.root = child
            return
        
        else:
            parent = self.find_parent_bst(root, data)
            
            if data <= parent.data:
                parent.left = child
    
            elif data > parent.data:
                parent.right = child    
        
        
    def add_node(self, parent, side, data):
        if parent == None or side == None or data == None:
            print "Error: adding child. check parameters"
            
        child = node(data)
        
        if str(side).lower() == "left":
            parent.left = child

        else:
            parent.right = child
            
                 
    def find_parent_bst(self, node, data):
        if node == None:
            return node

        while node:
            parent = node
            if data <= node.data:
                node = node.left
            else:
                node = node.right
        
        return parent
    
    
    def inorder_traversal(self, root):
        if root == None:
            return
        
        if self.inorder_traversal(root.left) != None:
            self.inorder_traversal(root.left)
            
        if root.data != None:
            self.tree_data_inorder.append(root.data)
            #print self.tree_data
            
        if self.inorder_traversal(root.right) != None:
            self.inorder_traversal(root.right)  
            
    
    def preorder_traversal(self, root):
        if root == None:
            return
            
        if root.data != None:
            self.tree_data_preorder.append(root.data)
            #print self.tree_data
            
        if self.preorder_traversal(root.left) != None:
            self.preorder_traversal(root.left)            
     
        if self.preorder_traversal(root.right) != None:
            self.preorder_traversal(root.right) 
            
            
    def postorder_traversal(self, root):
        if root == None:
            return
            
        if self.postorder_traversal(root.left) != None:
            self.postorder_traversal(root.left)            

        if self.postorder_traversal(root.right) != None:
            self.postorder_traversal(root.right)      
            
        if root.data != None:
            self.tree_data_postorder.append(root.data)
            #print self.tree_data        
            
    
    #display inorder data        
    def display_nodes(self):
        if self.root == None:
            return self.root
        
        self.tree_data_inorder = []
        self.inorder_traversal(self.root)
        print self.tree_data_inorder
        
    
    def get_tree_height(self, root):
        if root == None:
            return 0
        
        return max(self.get_tree_height(root.left),self.get_tree_height(root.right)) + 1
    
    
    def tree_height(self):
        return self.get_tree_height(self.root)
        
        

if __name__ == "__main__":
    tree_bt = tree(4) 
    tree_bt.add_node(tree_bt.root, "left", 3)
    tree_bt.add_node(tree_bt.root, "right", 5)
    tree_bt.add_node(tree_bt.root.left, "left", 2)
    
    tree_bt.display_nodes()
    
    
    
    tree_bst = tree(randint(0,9))
    for i in range(5):
        tree_bst.add_node_bst(tree_bst.root,randint(0,9)) 
        
    #tree_bst.display_nodes()
     
    tree_bst.inorder_traversal(tree_bst.root)
    print tree_bst.tree_data_inorder
    
    tree_bst.preorder_traversal(tree_bst.root)
    print tree_bst.tree_data_preorder


    tree_bst.postorder_traversal(tree_bst.root)
    print tree_bst.tree_data_postorder   