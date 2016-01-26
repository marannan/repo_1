import sys
import os


class node:
    def __init__(self,data=None):
        self.data = data # contains the data
        self.next = None # contains the reference to the next node
    
    

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None 

    def add_node(self, data):
        if data != None:
            new_node = node(data) # create a new node
        
        if self.head == None:
            self.head = new_node
            return
        
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            
            cur_node.next = new_node
            self.tail = new_node

    
    def add_nodes(self, data_array):
        for data in data_array:
            self.add_node(data)    

        
    def del_node(self, data):
        if self.head == None:
            print "node data in ll"
            return
    
        if self.head.data == data:
            self.head = self.head.next
            return
    
        cur_node = self.head
        pre_node = None        
        while cur_node:
            if cur_node.data == data:
                pre_node.next = cur_node.next
                return
    
            pre_node = cur_node
            cur_node = cur_node.next
    
        print "data not found"

        

    def display_nodes(self):
        if self.head == None:
            print "node data in ll"
            return        

        cur_node = self.head 
        while cur_node:
            print cur_node.data
            cur_node = cur_node.next

            
    def search_node(self, data):
        if head == None:
            print "node data in ll"
            return
    
        if head.data == data:
            return head

        cur_node = self.head
        pre_node = None        
        while cur_node:
            if cur_node.data == data:
                return cur_node
            cur_node = cur_node.next
        
        print "data not found"        
        
    def get_head(self):
        return self.head
    
    def set_head(self, new_head):
        self.head = new_head
            

if __name__ == "__main__":
    ll = linked_list()
    
    ll.add_nodes([4,7,8,9])
    head = ll.del_node(9)
    ll.display_nodes()        
    
    ll.del_node(0)
    ll.display_nodes()    
    