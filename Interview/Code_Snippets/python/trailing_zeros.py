#imports

#explanation

#How many multiples of 5 are between 1 and 23? There is 5, 10, 15, and 20, for four multiples of 5. 
#Paired with 2's from the even factors, this makes for four factors of 10, so:
#23! has four trailing zeroes 

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
    
    #int trailingZeroes(int n) {
        #int result = 0;
        #for(long long i=5; n/i>0; i*=5){
            #result += (n/i);
        #}
        #return result;
    #}    
        
if __name__ == "__main__":
    solution = Solution()
    #print solution.factorial(5)
    print solution.trailingZeroes(5)
    