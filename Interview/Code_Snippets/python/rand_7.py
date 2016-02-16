#generate rand_7() given rand_5() 
#naive approach

def rand_7():

    val = rand_5() + rand_5()
    return val % 7

#this would generate all values 0-6 wtih equal probability

#best solution

def _rand_7_best():
    
    val = 5 * rand_5() + rand_5
    
    if val < 21:
        return val % 7