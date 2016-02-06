

def no_of_1s(no):
    count = 0
    while no:
        if no & 1:
            count += 1
        
        no = no >> 1
        
    return count

if __name__ == "__main__":
    print no_of_1s(15)