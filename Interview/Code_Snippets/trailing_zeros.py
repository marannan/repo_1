#imports

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if  n >= 5:
            return self.trailingZeroes(n/5) + n/5
        else:
            return 0
    
    def factorial(self, n):
        if n == 1:
            return 1
        
        return n*self.factorial(n-1)
        
if __name__ == "__main__":
    solution = Solution()
    print solution.factorial(5)
    print solution.trailingZeroes(5)