
#Idea is to keep adding all the ele­ments to the cur_sum
#check if cur_sum > sum if yes remove first and check again and keep doing it until cur_sum > sum and move starting index
#check if cur_sum == sum then add elements from start to i+1 and return the sub_array


def continuous_sub_array_with_sum(array, sum):

    if len(array) <= 0:
        return array
    
    sub_array = []
    cur_sum = 0
    start = 0
    
    for i in range(len(array)):

        cur_sum = cur_sum + array[i]
        
        while cur_sum > sum:
            cur_sum = cur_sum - array[start]
            start = start + 1
            
        if cur_sum == sum:
            for j in range(start,i + 1):
                sub_array.append(array[j])
            return sub_array
                 
            
    return sub_array

def continuous_sub_array_with_sum(array, sum):

    if len(array) <= 0:
        return array
    
    sub_array = []
    cur_sum = 0
    start = 0
    
    for i in range(len(array)):

        cur_sum = cur_sum + array[i]
        
        while cur_sum > sum:
            cur_sum = cur_sum - array[start]
            start = start + 1
            
        if cur_sum == sum:
            for j in range(start,i + 1):
                sub_array.append(array[j])
            return sub_array
                 
            
    return sub_array

if __name__ == "__main__":
    if len(continuous_sub_array_with_sum([25, 12, 14, 22, 19, 15, 10, 23], 26)) == 0:
        print "no"
    else:
        print "yes"
    