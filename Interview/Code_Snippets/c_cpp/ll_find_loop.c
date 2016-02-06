Node* findCycleBegin(Node* head) 
{ 
    if (head == NULL) 
    { 
        return nullptr; 
    } 
 
  
    Node* slow = head; 
    Node* fast = head; 
    int diff = 0; 
 
  
    while (fast != NULL && fast->next != NULL) 
    { 
        slow = slow->next; 
        fast = fast->next->next; 
 
  
        if (slow == fast) // a collision 
        { 
            break; 
        } 
    } 
 
  
    // a check to make sure that there was in fact a loop 
    if (fast == NULL || fast->next == NULL) 
    { 
        return nullptr; 
    } 
  
    // slow is set to the head and then both are moved at the same pace 
    slow = head; 
    while (slow->next != fast->next) 
    { 
        slow = slow->next; 
        fast = fast->next; 
    } 
  
    // breaking the loop 
    fast->next = NULL; 
 
  
    // once they meet, they are at the start of the loop 
    return slow->next; 
  
} 