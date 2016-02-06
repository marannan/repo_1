hash_table = {}

def to_string(list):
    return "".join(list)

def check_hash_table(item):
    if item in hash_table.keys():
        return True
    else:
        hash_table[item] = True
        return False
    
    
def remove_dup(array):
    
    if len(array) <= 1:
        return array
    
    
    for i in range(len(array)):
        if check_hash_table(array[i]) == True:
            del array[i]
        
            
      
    return array
 
if __name__ == "__main__":
    print remove_dup([1,2,4,4])
    print remove_dup(list("ashokk"))
    print to_string(set(list("ashokk")))
            
        