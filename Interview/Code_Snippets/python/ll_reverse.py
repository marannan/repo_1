from ll import *

def linked_list_reverse(ll):
    if ll.head == None:
        return None
    
    ll_rev = ll
    cur_node = ll_rev.head
    pre_node = None
    next_node = None
    
    while cur_node:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node
        
    ll_rev.head = pre_node
    
    return ll_rev
    

if __name__ == "__main__":
    ll = linked_list()
    ll.add_nodes([7,6,5])
    ll.display_nodes()
        
    ll_rev = linked_list_reverse(ll)
    
    ll_rev.display_nodes()
    
    
    
    
    
    
        

