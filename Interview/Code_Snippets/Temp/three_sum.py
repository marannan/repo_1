

hash_table = {}

def get_from_hash_table(value_1, value_2):

    if value_2 in hash_table:
        return True
    
    else:
        hash_table[value_1] = True
    
    return False


def two_sum(nums, sum):
    #sum_pairs = []
    if len(nums) == 0:
        return None, None
    
    else:
        for i in range(0,len(nums)):
            if get_from_hash_table(nums[i], sum - nums[i]):
                return nums[i], sum-nums[i]
                        
    return None, None

    
def three_sum(nums, sum):
    global hash_table
    if len(nums) == 0:
        return None

    three_sum = []
    for i in range(len(nums)-2):
        num_2, num_3 = two_sum(nums[i+1:], sum-nums[i])
        if num_2 and num_3:
            three_sum.append([nums[i],num_2, num_3])
        hash_table = {}
            
        
        
    return three_sum

if __name__ == "__main__":
    print three_sum([1,2,3,4,5,6],15)
    