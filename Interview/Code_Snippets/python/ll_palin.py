#ll palindrome
#push half of the list into stack and pop the stack and check with remaning half of the list
#reverse and check

from ll import *
from ll_reverse import *

def linked_list_palin(ll_1, ll_2):
    if ll_1.head == None or ll_2.head == None:
        return False
    
    cur_1 = ll_1.head
    cur_2 = ll_2.head
    
    while cur_1 and cur_2:
        if cur_1.data != cur_2.data:
            return False
        cur_1 = cur_1.next
        cur_2 = cur_2.next
    
    if cur_1 or cur_2:
        return False
    
    return True


if __name__ == "__main__":
    
    ll_1 = linked_list()
    ll_1.add_nodes(['m','a','d'])
    ll_1.display_nodes()
    
    ll_2 = linked_list()
    ll_2.add_nodes(['m','a','d'])
    ll_2.display_nodes()    
 
    
    
    print linked_list_palin(ll_1, ll_2)
    
    
    