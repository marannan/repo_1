from ll import *
from ll_reverse import *

def linked_lists_add(ll_1, ll_2):
    if ll_1.head == None and ll_2.head == None:
        return None
    
    elif ll_1.head != None and ll_2.head == None:
        return ll_1

    elif ll_1.head == None and ll_2.head != None:
        return ll_2
    
    else:
        cur_1 = ll_1.head
        cur_2 = ll_2.head
        ll_added = linked_list()
        cur_3 = ll_added.head
        carry = 0
        sign = 1
        while cur_1 and cur_2:
            new_data = cur_1.data + cur_2.data + carry
            if new_data < 0:
                sign = -1
            new_data_add = ((new_data * sign) % 10) * sign
            carry = ((new_data * sign) / 10) * sign
            new_node = node(new_data_add)
            if ll_added.head == None:
                ll_added.head = new_node
            else:
                cur_3.next = new_node
            
            cur_3 = new_node
            cur_1 = cur_1.next
            cur_2 = cur_2.next

        while cur_1:
            new_data = cur_1.data + carry
            if new_data < 0:
                sign = -1            
            new_data_add = ((new_data * sign ) % 10) * sign
            carry = ((new_data * sign) / 10) * sign
            new_node = node(new_data_add)
            cur_3.next = new_node
            cur_3 = new_node
            cur_1 = cur_1.next
            
        
        while cur_2:
            new_data = cur_2.data + carry
            if new_data < 0:
                sign = -1            
            new_data_add = ((new_data * sign) % 10) * sign
            carry = ((new_data * sign) / 10) * sign
            new_node = node(new_data_add)
            cur_3.next = new_node
            cur_3 = new_node
            cur_2 = cur_2.next        
            
        
        if carry != 0: 
            new_node = node(carry)
            cur_3.next = new_node
            
                
        
        return ll_added
        
#recursive handles negative nos
def linked_lists_add_2(node_1, node_2, carry=0):
    
    if node_1 == None and node_2 == None and carry == 0:
        return None
    
    value = carry
    
    if node_1:
        value = value + node_1.data
        
    if node_2:
        value = value + node_2.data
        
    
    new_node = node()
    if value >= 0:
        new_node.data = value % 10
        carry = value / 10
    
    else: #handle the negative case
        new_node.data = (-1) * ((value * -1) % 10) 
        carry = (-1) * ((value * -1) / 10) 

    if node_1 == None:
        next_1 = None
    
    else:
        next_1 = node_1.next
        
    if node_1 == None:
        next_2 = None    
        
    else:
        next_2 = node_2.next
    
     
    new_node.next = linked_lists_add_2(next_1, next_2, carry)
    
    
    return new_node

if __name__ == "__main__":
    ll_1 = linked_list()
    ll_2 = linked_list()
    
    ll_1.add_nodes([9])
    ll_2.add_nodes([-9,-9])
    
    ll_1_rev = linked_list_reverse(ll_1)
    ll_2_rev = linked_list_reverse(ll_2)
    #ll_1_rev.display_nodes()
    #ll_2_rev.display_nodes()

    
    #linked_list_reverse(add_linked_lists(ll_1_rev,ll_2_rev)).display_nodes()
    
    ll_add = linked_list()
    ll_add.head = linked_lists_add_2(ll_1_rev.head, ll_2_rev.head, 0)
    linked_list_reverse(ll_add).display_nodes()
    
    return
    
    
    