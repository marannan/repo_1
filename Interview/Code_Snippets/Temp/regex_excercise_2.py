import re

class Solution:
    def is_match(self, str_1, str_2):
        if str_1 == str_2:
            return True
        
        if str_2 == ".*":
            return True
        
        if str_2 == ".":
            if len(str_1) == 1:
                return True
        
    
        
        

if __name__ == "__main__":
    solution = Solution()
    print solution.is_match("aa", "aa")