#create a binary string of length equal to n
#each bit can be 0 or 1
#start with index = 0
#set binary_string[index] = 0 and other bits can be anything so recurse with index++
#set binary_string[index] = 1 and other bits can be anything so recurse with index ++ 
#base condition is index == lenght of set just print the binary_string


bit_array = [-1] * 1000

def n_bit_strings(n, index = 0):
    
    if index == n:
        print bit_array[:n]


    else:
        bit_array[index] = 0
        n_bit_strings(n, index + 1)
        bit_array[index] = 1
        n_bit_strings(n, index + 1)


if __name__ == "__main__":
    n_bit_strings(3)