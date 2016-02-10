
#move tower of top n - 1 from source to helper using target as helper
#move top from source to target
#move tower of top n-1 from helper to target using source as helper


def hanoi(n, source, helper, target):
    if n <= 0:
        return 
    
    else:
        #move tower of top n - 1 from source to helper using target as helper
        hanoi(n - 1, source, target, helper)
        
        #move top from source to target
        if source:
            target.append(source.pop())
            
        #move tower of top n-1 from helper to target using source as helper
        hanoi(n - 1, helper, source, target)


if __name__ == "__main__":        
    source = [4,3,2,1]
    target = []
    helper = []
    hanoi(len(source),source,helper,target)
    
    print source, helper, target