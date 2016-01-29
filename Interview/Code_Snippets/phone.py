
phone_nos = {2:['a','b','c'],
3:['d','e','f'],
4:['g','h','i'],
5:['j','k','l'],
6:['m','n','o'],
7:['p','q','r'],
8:['s','t','v'],
9:['w','x','y','z'],}

def get_letters(no):
    if no == None:
        return []
    
    letters = []
    digits = []
    while no > 0:
        digits.append(no%10)
        no = no/10
        
    digits = list(reversed(digits))
    
    letters_list = []
    for digit in digits:
        letters_list.append(phone_nos[digit])
    
    string = []
    get_combinations(digits, 0, string)

    for letter_list in letters_list:
        print letter_list
    
    #result=[]
    #out=[None]*len(digits)
    
    #def print_letter(index):
        #if (index==len(digits)-1): 
            #for letter in letters_list[index]:
                #out[index]=letter
                #result.append(out[:])
        #else:
            #for letter in letters_list[index]:
                #out[index]=letter
                #print_letter(index+1)
    #print_letter(0)
    #return result
    
 

def get_combinations(digits,index,string):
    
    if index == len(digits):
        print string
        string.pop()
        return
        
    
    #if digits[index] == 0 or digits[index] == 1:
        #return
    
    for i in range(len(phone_nos[digits[index]])):
        char_list = phone_nos[digits[index]]
        string.append(char_list[i])
        get_combinations(digits, index+1, string)
    
    
    
if __name__ == "__main__":
    print get_letters(23)
    