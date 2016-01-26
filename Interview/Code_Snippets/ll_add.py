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
        while(cur_1 and cur_2):
            new_data = cur_1.data + cur_2.data + carry
            new_data_add = new_data % 10
            carry = new_data / 10
            new_node = node(new_data_add)
            if ll_added.head == None:
                ll_added.head = new_node
            else:
                cur_3.next = new_node
            
            cur_3 = new_node
            cur_1 = cur_1.next
            cur_2 = cur_2.next
            
        if carry > 0:
            new_node = node(carry)
            cur_3.next = new_node
        
        return ll_added
        

if __name__ == "__main__":
    ll_1 = linked_list()
    ll_2 = linked_list()
    
    ll_1.add_nodes([2,4,3])
    ll_2.add_nodes([5,6,4])
    
    #ll_1.display_nodes()
    #ll_2.display_nodes()

    
    add_linked_lists(ll_1,ll_2).display_nodes()
    
    
    
    