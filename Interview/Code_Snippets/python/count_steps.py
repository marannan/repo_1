#count steps
#top to bottom approcah
#last nth step can be reached by 1 hop from n-1th step or 2 hop from n-2th step or 3 hop from n-3th step
#so total no of ways reaching the last step is sum of total no of ways of reaching each of the last three steps

#for caching results
steps_count_cache = [False]*1000

def count_steps_dp(n):
    if n < 0:
        return 0
    
    if n == 0: #there is one way to climb 0 steps ie is you dont have to do anything
        return 1
    
    if steps_count_cache[n]:
        return steps_count_cache[n]
    
    steps_count_cache[n] = count_steps_dp(n-1) + count_steps_dp(n-2) + count_steps_dp(n-3) 
    
    return steps_count_cache[n]

if __name__ == "__main__":
    print count_steps_dp(0)