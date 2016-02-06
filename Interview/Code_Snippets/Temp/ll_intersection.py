
hash_table = {}

def add_hash(item):
    if item in hash_table:
        return True
    else:
        hash_table[item] = True
        return False


def find_intersection(list_1, list_2):
    list_inter = []
    
    if list_inter.count == 0 or list_2.count == 0:
        return list_inter    
     
    for item in list_1:
        add_hash(item)
        
    for item in list_2:
        if add_hash(item) == True:
            list_inter.append(item)
            
    return list_inter
    

if __name__ == "__main__":
    print find_intersection([1,2,3,4], [4,1])
        