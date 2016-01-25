import sys
import os




def is_palin(string):
    
    if len(string) == 0:
        return False
    
    i = 0
    j = len(string) - 1
    
    
    while i < j:
        if str(string[i]).isalpha()== False:
            i = i + 1;
            continue
        if str(string[j]).isalpha() == False:
            j = j - 1;        
            continue

        if string[i] != string[j]:
            return False
        i = i + 1
        j = j - 1
        
    return True


def main():
    string = sys.argv[1]
    
    if is_palin(string) == True:
        print "yes"
    else:
        "no"
    
    
    return
if __name__ == "__main__":
    main()