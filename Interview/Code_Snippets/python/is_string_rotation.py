#check if s2 is rotation of s1

#idea
#****
#check if rotated string is a substring on s1+s1
#because waterbottlewaterbottle will form was complete rotation and roatation of waterbottle = erbottlewat will present 

def is_rotation(string_1, string_2):
    string_3 = string_1 + string_1
    
    return str(string_2) in string_3

if __name__ == "__main__":
    print is_rotation("waterbottle", "erbottlewat")
    