#generate all possible permutations of a string
#idea
#****
#to get permutations of a string of len = 1 str = "A" insert A in all possible positions of ""
#to get permutations of a string of len = 2 str = "AB" split string into first and rest 
#insert A in all possible positions of "" => "A" 
#and insert B in all possible positions of "A" => "BA" and "AB" 
#to get permutations of string of len = 3 str = "ABC" insert C in all possible positions of string from above

#algo
#****
#string = "ABC"
#split first and rest
#recurse until len(rest) == 0 then return list with empty string "" as string_list
#so last recursion will have first = C and string_list = [""]
#for every word in string_list insert C at all possible places in. ie start, middle and end
#add each insertion to a list and return

#tracing for "ABC"
#*****************
#1.string = "ABC"
#2.first = "A" rest = "BC" recurse("BC")
#3.first = "B" rest = "c" recurse("C")
#4.first = "C" rest = "" recurse("")
#5.len("") == 0 so return [""] to line 4 (first = "C" rest = "" recurse(""))
#first = "C" string_list = [""]
#for every word in string_list ie ""
#insert first = "C" in all possible places to result words
#result = "c"
#prem.add(result)
#return ["C"] to line 3 (first = "B" rest = "C" recurse("C"))
#first = "B" string_list = ["C"] 
#for word in string_list ie "C"
#insert first = "B" in all possible places to form result words
#result words = "BC" (B at staring) and "CB" (B at ending)
#return ["BC", "CB"] to line 2 (first = "A" rest = "BC" recurse("BC"))
#first = "A" rest = "BC" recurse("BC")
#for every word in string_list ie "BC" , "CB"
#insert first = "A" at all possible positions to form result words
#for word "BC" insert "A" at starting  = "ABC" at middle "BAC" at ending "BCA"
#add all results words to list
#for word "CB" insert "A" at starting  = "ACB" at middle "CAB" at ending "CBA"
#return result words list to line 1 to return back


def string_permute(string):
    
    
    if len(string) == 0:
        return [""]
    
    else:
        first = string[0]
        rest = "".join(list(string)[1:])
        
        string_list = string_permute(rest)
        
        perm = []
        for word in string_list:
            for i in range(0,len(word)+1):
                result = word[0:i] + first + word[i:len(word)]
                perm.append(result)
        
    return perm

if __name__ == "__main__":
    print string_permute("ABC")
