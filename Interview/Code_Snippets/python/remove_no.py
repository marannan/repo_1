
def remove_no(array, no):
    if len(array) == 0:
        return array
    
    begin = 0
    for i in range(len(array)):
        if array[i] != no:
            array[begin] = array[i]
            begin  = begin + 1
            
    
    return array[:begin]

if __name__ == "__main__":
    print remove_no([1,2,2,3,4,2], 2)
