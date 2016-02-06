from ll import *
from ll_reverse import *

def add_linked_lists(ll_1, ll_2):
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
        

if __name__ == "__main__":
    ll_1 = linked_list()
    ll_2 = linked_list()
    
    ll_1.add_nodes([-9])
    ll_2.add_nodes([9,9])
    
    ll_1_rev = linked_list_reverse(ll_1)
    ll_2_rev = linked_list_reverse(ll_2)
    #ll_1_rev.display_nodes()
    #ll_2_rev.display_nodes()

    
    linked_list_reverse(add_linked_lists(ll_1_rev,ll_2_rev)).display_nodes()
    
    
    
    