#partition list based on val x
#use head_1 and tail_1 for list < x and head_2 and tail_2 to list > x and merge them

from ll import *

def linked_list_partition(ll, val):
    if ll.head == None:
        return ll
    
    head_1 = node()
    head_2 = node()
    tail_1 = node()
    tail_2 = node()
    
    cur = ll.head
    #ll_part = linked_list()
    
    while cur:
        next_node = cur.next
        
        if cur.data < val:
            if head_1.data == None:
                head_1 = cur
                tail_1 = head_1
            else:
                tail_1.next = cur
                tail_1 = cur
        
        else:
            if head_2.data == None:
                head_2 = cur
                tail_2 = head_2
            else:
                tail_2.next = cur
                tail_2 = cur
                
        
        cur = next_node
    
    tail_2.next = None
    
      
    if head_1 == None:
        ll_part.head = head_2
        return ll_part
        
    
    #merge two lists
    tail_1.next = head_2
    
    #changing to new head
    ll.head = head_1
    
    return ll


if __name__ == "__main__":
    ll = linked_list()
    
    ll.add_nodes([4,5,2,1])
    #ll.display_nodes()
    
    ll_part = linked_list_partition(ll, 3)
    
    ll_part.display_nodes()
    
    return
    