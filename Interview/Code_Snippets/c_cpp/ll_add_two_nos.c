Node * add_recursive( Node * list1, Node * list2, int carry) 
{ 
    if ( list1 == nullptr && list2 == nullptr && carry == 0 ) 
    { 
      return nullptr; 
    } 

    int value = carry; 
    if ( list1 ) 
    { 
      value += list1->data; 
    } 
    if ( list2 ) 
    { 
      value += list2->data; 
    } 


    Node * resultNode = new Node( value % 10 ); 


    resultNode->next = add_recursive( list1 ? (list1->next) : nullptr, 
                                      list2 ? (list2->next) : nullptr, 
                                      value > 9 ? 1 : 0 ); 
    return resultNode; 
}