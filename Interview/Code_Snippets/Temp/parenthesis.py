def is_valid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

def is_valid_2(string):
    if string == None:
        return False
    
    stack = []
    parenthesis = {'}':'{', ')':'(', ']':'['}
    
    for char in string:
        if char in parenthesis.values():
            stack.append(char)
        else:
            if parenthesis[char] != stack.pop():
                return False
    
    return stack == []

if __name__ == "__main__":
    print is_valid_2("{([)}")