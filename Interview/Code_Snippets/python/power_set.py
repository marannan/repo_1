#generate power set
#no of subsets = 2^n because each element can either be present or absent in each set
#O(2^n)
#yes = 1 and no = 0
#create a binary string of length equal to length the set
#each index values can be 0 or 1
#start with index = 0
#set binary_string[index] = 0 and recurse with index++
#set binary_string[index] = 1 and recurse with index ++ 
#base condition is index == lenght of set just print the binary_string


global bit_array
global set

def power_set_2(index = 0):
     if index == len(set):
          sub_set = []
          for i in range(0, len(bit_array)):
               if bit_array[i] == 0:
                    continue
               else:
                    sub_set.append(set[i])
          print sub_set
          sub_set = []
               
     
     else:
          bit_array[index] = 0
          power_set_2(index + 1)
          bit_array[index] = 1
          power_set_2(index + 1)
               
          
                    
if __name__ == "__main__":
     global bit_array, set
     set = [1,2,3]
     bit_array = [-1] * len(set)
     
     power_set_2()