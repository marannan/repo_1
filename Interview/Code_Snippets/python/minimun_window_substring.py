#Idea 
#****
#keep two pointers left and right.
#If s[left:right] has all chars in T, calculate distance and keep answer, then move left pointer.
#If s[left:right] doesn't have all chars in T, move right pointer.


# @param {string} s
# @param {string} t
# @return {string}
# sliding window problem
# count all chars in string T
# left pointer point to string which has been processed
# right pointer point to string, which has not been processed
# 1.if all window from left to right contains all string T(counter values all less then or equal to 0)
#   calculate min window length, and keep answer
#   then move left pointer
# 2.else there are missing string in current answer
#   move right pointer
#   update counter
# repeat 1, 2 steps until right is equal to len(s), then break it

import collections

def min_window(s, t):
    left, right = 0, 0
    # count T chars
    counter = {}#collections.defaultdict(int)
    for a in t:
        if a in counter:
            counter[a] += 1
        else:
            counter[a] = 1

    minwindow = len(s) + 1
    answer = None

    while right <= len(s):
        # check all chars in T are in the current answer
        
        counter_empty = True
        for char in counter:
            if counter[char] > 0:
                counter_empty = False
                break
        
        #if all(map(lambda x: True if x<=0 else False, counter.values())):
        if counter_empty == True:
            if minwindow > right-left:
                minwindow = right-left
                answer = s[left:right]
            char = s[left]
            if char in counter:
                counter[char] += 1
            left += 1
        else:
            if right == len(s):
                break
            char = s[right]
            if char in counter:
                counter[char] -= 1
            right += 1

    return answer if answer else ''


#Have a left and right pointer, initially both at zero
#Move the right pointer forwards until [L..R] contains all the elements (or quit if right reaches the end).
#Move the left pointer forwards until [L..R] doesn't contain all the elements. 
#See if [L-1..R] is shorter than the current best.
#keep track of how many of each element of B is in the subarray for checking whether the subarray is a potential solution.

#Pseudocode of this algorithm.

#size = bestL = A.length;
#needed = B.length-1;
#found = 0; left=0; right=0;
#counts = {}; //counts is a map of (number, count)
#for(i in B) counts.put(i, 0);

#//Increase right bound
#while(right < size) {
    #if(!counts.contains(right)) continue;
    #amt = count.get(right);
    #count.set(right, amt+1);
    #if(amt == 0) found++;
    #if(found == needed) {
        #while(found == needed) {
            #//Increase left bound
            #if(counts.contains(left)) {
                #amt = count.get(left);
                #count.set(left, amt-1);
                #if(amt == 1) found--;
            #}
            #left++;
        #}
        #if(right - left + 2 >= bestL) continue;
        #bestL = right - left + 2;
        #bestRange = [left-1, right] //inclusive
    #}
#}


if __name__ == "__main__":
    print min_window("ADOBECODEBANC", "ABC")