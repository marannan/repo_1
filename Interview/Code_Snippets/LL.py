import sys
import os


class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.head_node = None
        self.tail_node = None      

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = None 
        
        if self.head_node == None:
            self.head_node = new_node
        
        else:
            cur_node = node()
            cur_node = self.head_node
            while cur_node.next:
                cur_node = cur_node.next
            
            cur_node.next = new_node
            self.tail_node = new_node
        
    def del_node(self, data):
        cur_node  = node()
        cur_node = self.head_node
        pre_node = node()

        if self.head_node == None:
            print "node data in ll"
            return
        
        if self.head_node.data == data:
            self.head_node = self.head_node.next
        
        while cur_node:
            if cur_node.data == data:
                pre_node.next = cur_node.next
                return
            
            pre_node = cur_node
            cur_node = cur_node.next
        
        print "data not found"
        

    def list_print(self):
        if self.head_node == None:
            print "node data in ll"
            return        

        cur_node = node()
        cur_node = self.head_node 
        while cur_node:
            print cur_node.data
            cur_node = cur_node.next
            
    def get_head(self):
        return self.head_node
    
            
        

if __name__ == "__main__":
    ll = linked_list()
    ll.list_print()
    for i in range(4):
        ll.add_node(i)
            
    ll.list_print()
    
    ll.del_node(5)
    ll.list_print()