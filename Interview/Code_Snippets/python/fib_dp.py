#fibbonaci in dp
#cache fib of values to avoid recalculating 

fib_cache = [False]*1000
def fib_dp(n):
    if n <= 1:
        return n
    
    if fib_cache[n]:
        return fib_cache[n]
    
    fib_cache[n] = fib_dp(n-1) + fib_dp(n-2)
    
    return fib_cache[n]

if __name__ == "__main__":
    print fib_dp(10)