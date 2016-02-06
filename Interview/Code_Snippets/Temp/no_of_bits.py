

def no_of_bits(no):
    
    i = 0
    
    while pow(2,i) <= no:
        i += 1
        
    return i

if __name__ == "__main__":
    print no_of_bits(2)