#tree
class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
        
    
class tree:
    def __init__(self):
        self.root = None
        
    def add_node(self, data):
        if data != None:
            child = node(data)
          
        #print "current tree before adding node"
        #self.display_nodes()
        
        if self.root == None:
            self.root = child
            #print "current tree after adding node"
            #self.display_nodes()            
            return
    
        parent = self.find_parent(self.root, data)
        if data <= parent.data:
            parent.left = child
        else:
            parent.right = child
        
        #print "current tree after adding node"
        #self.display_nodes()
                 
    def find_parent(self, node, data):
        if node == None:
            return node

        if data <= node.data:
            parent = node
            if self.find_parent(node.left, data) == None:
                return parent
        
        if data > node.data:
            parent = node
            if self.find_parent(node.right, data) == None:
                return parent
        
    def in_order_traversal(self, root):
        if root == None:
            return
        
        if self.in_order_traversal(root.left) != None:
            print self.in_order_traversal(root.left)
        if root.data != None:
            print root.data
        if self.in_order_traversal(root.right) != None:
            print self.in_order_traversal(root.right)        
            
    def display_nodes(self):
        if self.root == None:
            return self.root
        
        self.in_order_traversal(self.root)
        
        

if __name__ == "__main__":
    tree = tree()
    for i in range(5):
        tree.add_node(i)
    #tree.add_node(0)
    #tree.add_node(2)
    tree.display_nodes()
    
    
        
        
        
        