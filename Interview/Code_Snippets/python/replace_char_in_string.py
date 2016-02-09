

def replace(string, replace_to, replace = " "):
    if len(string) == 0 or len(replace_to) == 0:
        return string
    
    return string.replace(replace, replace_to)

if __name__ == "__main__":
    print replace("orange color", "%20", " ")
    