
def to_string(prefix):
    return "".join(prefix)

#take first char in first word and check if its the first char of all words
#continue with second 
#stop if atleast one word doesnt have the char that is being matched
#return the first word until last matched char

def longest_prefix(str_list):
    if len(str_list) == 0:
        return ""
    
    prefix = []
    break_flag = False
        
    break_flag = False
    first_string = str_list[0]
    for i in range(len(first_string)):
        for string in str_list[1:]:
            if i == len(string):
                break_flag = True
                break
            if first_string[i] != string[i]:
                break_flag = True
                break
        
        if break_flag == False:
            prefix.append(first_string[i])
        else:
            break
        
        
        
        
    return to_string(prefix)
    
    
if __name__ == "__main__":
    print longest_prefix([['a','s','s','o','k'],['a','s','s']])