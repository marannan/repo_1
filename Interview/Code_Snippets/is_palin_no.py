class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
    
        div = 1        
        while x / div >= 10:
            div = div * 10
    
        while x > 0:
            #print x
            p = x / div
            q = x % 10
    
            if p != q:
                return False
    
            else:
                x = (x % div) / 10 
                div = div / 100    

        return True        

if __name__ == "__main__":
    sol = Solution()
    print sol.isPalindrome(1201)