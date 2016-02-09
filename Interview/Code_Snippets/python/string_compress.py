
#return compressed string. Ex: "aabcccccaaa" = "a2b1c5a3"
#return original string if length of original is smaller. Ex: len("a" ) < len("a1") so return "a"

def str_compress(string):
    if len(string) < 1:
        return string
    
    string_comp  = ""
    count  = 1
    last_seen = string[0]
    
    for i in range(1,len(string)):
        if string[i] == last_seen:
            count = count + 1
        else:
            string_comp = string_comp + last_seen + str(count)
            last_seen = string[i]
            count = 1
    
    
    string_comp = string_comp + last_seen + str(count)
    
    if len(string) < len(string_comp):
        return string
    else:
        return string_comp
    

if __name__ == "__main__":   
    print str_compress("aabcccccaaa")