#sort stack in ascending order
#use one more stack for sorting
#pop from stack_1 and push into right position on stack_2


def sort_stack(stack_1, stack_2):
    if len(stack_1) <= 1:
        return stack_1
    
    while len(stack_1) > 0:
        temp = stack_1.pop()
     
        while len(stack_2) != 0 and stack_2[len(stack_2)-1] > temp:
            item  = stack_2.pop()
            stack_1.append(item)
            
        stack_2.append(temp)
        
    
    return stack_2


if __name__ == "__main__":
    print sort_stack([8,5,10,7,3,9,6,1,2],[])
            
        
        
        
        
  
  