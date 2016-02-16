#imports

#explanation
#count pair of multiples of 5 and 2 => just count of multiples of 5
#How many multiples of 5 are between 1 and 23? There is 5, 10, 15, and 20, for four multiples of 5. 
#Paired with 2's from the even factors, this makes for four factors of 10, so:
#23! has four trailing zeroes 

class Solution(object):
    
    #counting no of factors of 5 then 25 and 125 and so on
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if  n >= 5:
            return self.trailingZeroes(n/5) + n/5
        else:
            return 0
     
    def factor_of_5(self, i):
        count = 0
        
        while i % 5 == 0:
            count  = count + 1
            i = i / 5 
            
        return count
        
    def trailing_zeros(self, n):
        
        trailing_zeros = 0
        #count no of 5s in n
        for i in range(2,n):
            trailing_zeros = trailing_zeros + self.factor_of_5(i)
            
        return trailing_zeros
        
    
    def factorial(self, n):
        if n == 1:
            return 1
        
        return n*self.factorial(n-1)
    
    #couting factors of five
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
    print solution.trailing_zeros(21)
    