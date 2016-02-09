#remove duplicates from list
#use hash if no space constraint is given (not implemeted)
#else do loop for each node and check the data for dups and change the next pointers

from ll import *

def linked_list_remove_duplicates(ll):
    if ll.head == None:
        return ll
    
    cur = ll.head
    
    while cur:
        runner  = cur
        
        while runner.next:
            if runner.next.data == cur.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
                
        cur = cur.next
        
    return ll


if __name__ == "__main__":
    ll = linked_list()
    
    ll.add_nodes([1,2,2,3,5,5,6])
    #ll.display_nodes()
    
    ll_no_dups = linked_list_remove_duplicates(ll)
    
    ll_no_dups.display_nodes()
    