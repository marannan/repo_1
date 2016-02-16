#find two elements that sum upto x in an array
#idea
#****
#use hash and find element - sum is in hash else add element to hash

#alternate solution
#sort and use first and last pointer and add them to see sum  = x else move first or reduce last

hash_table = {}

class Solution(object):
    

    def get_from_hash_table(self, value_1, index, value_2):

        if value_2 in hash_table:
            return hash_table[value_2]
        
        else:
            hash_table[value_1] = index
        
        return -1
    
    
    def twoSum(self, nums, target):
        #sum_pairs = []
        if len(nums) == 0:
            return False
        
        else:
            for i in range(0,len(nums)):
                index = self.get_from_hash_table(nums[i], i, target - nums[i])
                if index > -1:
                    if i < index:
                        return [i+1,index+1]
                    else:
                        return [index+1,i+1]
                    
                
                
        return 0
        

if __name__ == "__main__":
    solution = Solution()
    print solution.twoSum([2,1,9,4,4,56,90,3], 8)