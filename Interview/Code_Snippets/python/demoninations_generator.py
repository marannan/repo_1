#no of ways to make change for n cents using demoninations (quaters(25c), dimes(10c), nickels(5c) and pennies(1c) )

#idea 
#****
#making change for 100 cents will involve either 0, 1, 2, 3 or 4 quaters
#no of ways is
#make_change(100c using 0q) + 
#make_change(100c using 1q) + 
#make_change(100c using 2q) +
#make_change(100c using 3q) + 
#make_change(100c using 4q)

#make_change(100c using 1q) is reduced to make_change(75c using 0q) like first and so on
#so use recursion 
#extend this to all other demoninations

def make_change(total_amount, demoninations, dp_map, index = 0):
    
    #retrieve from dp_map to reduce the time 
    #if change available for the amount in that demonination just return
    if dp_map[index][total_amount - 1] > 0:
        return dp_map[index][total_amount - 1]
    
    #base case of one last demonination equivalent amount remaining
    if index >= len(demoninations) - 1:
        return 1
    
    #start with quaters and move
    denom = demoninations[index]
    
    no_ways = 0
    
    #calculation no of ways using other denoms when you have i no of current denom
    for i in range(0,total_amount):
        #stop calculating when i times the denom >= total amount. example 4times * 25(quaters) = 100 stop
        if i * denom >= total_amount:
            break
        
        #find no of ways the remaining amount can be made using other denoms 
        #because you've used amount equivalent to i times curent denom 
        amount_rem = total_amount - i * denom
        no_ways = no_ways + make_change(amount_rem, demoninations, dp_map, index + 1)
        
     
     
    #save the no of ways an amount can be made using given denom so that we dont have recalculate again during recursion
    dp_map[index][total_amount - 1] = no_ways
    
    return no_ways
    

if __name__ == "__main__":
    denominations = [25, 10, 5 , 1]
    quaters = [0] * 100
    dimes = [0] * 100
    nickels = [0] * 100
    pennies = [0] * 100
    
    dp_map = [quaters, dimes, nickels, pennies]
   
    print make_change(100, denominations, dp_map)