from ll import *
from ll_reverse import *

def find_mid(ll):
    if ll.head == None:
        return None
    
    slow = ll.head
    fast = ll.head
    
    #ll.display_nodes()
    
    while fast and fast.next:
        next = slow.next
        slow = slow.next
        fast = fast.next.next
    
    t = slow.next
    slow.next = None
    return t

def linked_list_first_last(ll_1,ll_2):
    if ll_1 == None:
        return ll_2
    
    elif ll_2 == None:
        return ll_1
    
    ll_3 = linked_list()
    ll_3.head = ll_1.head
    
    cur_1 = ll_1.head
    cur_2 = ll_2.head
    
    while cur_2:
        cur_1_next = cur_1.next
        cur_2_next = cur_2.next
        cur_1.next = cur_2
        cur_2.next = cur_1_next
        cur_1 = cur_1_next
        cur_2 = cur_2_next
        if cur_1 == None:
            break
         
    
    return ll_3
        
        

if __name__ == "__main__":
    ll = linked_list()
    ll.add_nodes([1,2,3,4,5,6])
    #ll.display_nodes()
    
    ll_last = linked_list()
    ll_last.head = find_mid(ll)
    
    #ll_last.head = ll_last.head.next
    ll_rev = linked_list_reverse(ll_last)
    
    #ll.display_nodes()
    #ll_rev.display_nodes()
    
    ll_3 = linked_list_first_last(ll,ll_rev)
    print ll_3.display_nodes()