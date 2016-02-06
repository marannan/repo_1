#imports



def multiply_lists(list_1, list_2):
    
    if list_1.count == 0 or list_2.count == 0:
        return list_multi
    
    list_1.reverse()
    list_2.reverse()
    for i in range(len(list_1)):
        carry = 0
        list_temp = []
        for q in range(i):
            list_temp.append(0)        
        for j in range(len(list_2)):
            k  =  int(list_1[i]) * int(list_2[j]) + carry
            multi = k % 10
            carry = k / 10
            list_temp.append(multi)
        if carry > 0:
            list_temp.append(carry)
            
        list_multi.append(list_temp)
        
    len_max = 0
    for lst in list_multi:
        length = len(lst)
        if length > len_max:
            len_max = length
            
    
    for lst in list_multi:
        for i in range(len_max - len(lst)):
            lst.append(0)
            
    res_list = []
    carry = 0
    for i in range(len_max):
        new_data = carry   
        for lst in list_multi:
            new_data = lst[i] + new_data
        carry = new_data/10
        res_list.append(new_data%10)
    
    
    res_list.reverse()
    return res_list
    
            
    
    

if __name__ == "__main__":
    string_1 = "2"
    string_2 = "1"
    list_multi = []
    list_multi =  multiply_lists(list(string_1),list(string_2))
    print list_multi