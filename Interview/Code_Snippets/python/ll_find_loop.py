
#find loop 
#return start of the loop
#break loop

def linked_list_find_loop(ll):
    if ll.head == None:
        return False, None, ll # returing True/False for loop found, start of loop, list after breaking the loop
    
    slow = ll.head
    fast = ll.head
    loop_found = False
    
    #find ll has a loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            loop_found = True
            break
    
    if loop_found == False:
        return loop_found, None, ll
    
    
    #find starting of loop
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
        
    
    loop_point = fast.next
    
    #breaking the loop
    fast.next = None
    
    return loop_found, loop_point, ll
