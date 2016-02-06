
#Idea is to keep adding all the ele­ments to the currSum
#Keep check­ing if the currSum<Sum
#If currSum gets greater than the Sum then start reduc­ing the currSum from the begin­ning of the array using “start“if any time currSum=Sum, Stop and return

def continuous_sub_array_with_max_sum(array, sum):

    if len(array) <= 0:
        return array
    
    sub_array = []
    cur_sum = 0
    start = 0
    
    for i in range(len(array)):
        
        while cur_sum > sum:
            cur_sum = cur_sum - array[start]
            start = start + 1
            
        if cur_sum == sum:
            for j in range(start,i):
                sub_array.append(array[j])
            return sub_array
                
        else:
            cur_sum = cur_sum + array[i]
                
            
        
    
    return sub_array

if __name__ == "__main__":
    print continuous_sub_array_with_max_sum([25, 12, 14, 22, 19, 15, 10, 23], 59)
    