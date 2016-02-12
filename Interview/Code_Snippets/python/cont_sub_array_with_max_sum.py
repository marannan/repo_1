#Kadane’s Algorithm:
#Initialize:
    #max_ending_here = 0
    #max_so_far = a[0]
    
#Loop for each element of the array
  #(a) max_ending_here = max_ending_here + a[i]
  #(b) if(max_so_far < max_ending_here)
            #max_so_far = max_ending_here
  #(c) if(max_ending_here < 0)
            #max_ending_here = 0
#return max_so_far


def max_continuous_sub_arrary(array):
    
    if len(array) == 0:
        return None
    
    if len(array) == 1:
        return array[0], [array[0]]
    
    max_now = array[0]
    max_total = array[0]
    end = 0
    
    for i in range(1,len(array)):
         
        max_now = max(array[i], max_now + array[i])        
        
        #save index as last as this element will be included if below condition is true which will update max_total
        if max(array[i], max_now + array[i]) > max_total:
            end = i        

        max_total = max(max_now, max_total)  
          
    sum = 0 
    start = 0
    for i in range(end, -1, -1):
        sum = sum + array[i]
        if sum == max_total:
            start = i
            break
            
    return max_total, array[start:end + 1]

def max_continuous_sub_arrary_2(array):
    
    if len(array) == 0:
        return None
    
    if len(array) == 1:
        return array[0], [array[0]]
    
    max_now = 0
    max_total = array[0]
    end = 0
    
    for i in range(0,len(array)):
        max_now = max_now + array[i]
        
        if max_total < max_now:
            max_total = max_now
            end = i
            
        if max_now < 0:
            max_now = 0
        
    sum = 0 
    start = 0
    for i in range(end, -1, -1):
        sum = sum + array[i]
        if sum == max_total:
            start = i
            break
            
    return max_total, array[start:end + 1]



if __name__ == "__main__":
    print max_continuous_sub_arrary_2([-2, -3, 4, -1, -2, 1, 5, -3])
        