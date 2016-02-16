#minimun insertions to make a string a palindrome
#O(n^2)
#idea
#****
#Recursive Solution
#The minimum number of insertions in the string str[l…..h] can be given as:
#minInsertions(str[l+1…..h-1]) if str[l] is equal to str[h]
#min(minInsertions(str[l…..h-1]), minInsertions(str[l+1…..h])) + 1 otherwise

def find_min_insertions_palin(string):

    #Create a table of size n*n. table[i][j] will store
    #minumum number of insertions needed to convert str[i..j]
    #to a palindrome.
    
    # Creates a list containing 5 lists initialized to 0
    table = [[0 for x in range(len(string) + 1)] for x in range(len(string) + 1)] 
    
    l = 0
    n = len(string)

    #Fill the table
    for gap in range (1, n):
        l = 0
        for h in range(gap,n):
            if string[l] == string[h]:
                table[l][h] = table[l+1][h-1] 
            else:
                table[l][h] = min(table[l][h-1], table[l+1][h]) + 1
            l = l + 1
 
    #Return minimum number of insertions for str[0..n-1] or str[l...h]
    return table[0][n-1]


#Another Dynamic Programming Solution (Variation of Longest Common Subsequence Problem)
#The problem of finding minimum insertions can also be solved using Longest Common Subsequence (LCS) Problem. If we find out LCS of string and its reverse, we know how many maximum characters can form a palindrome. We need insert remaining characters. Following are the steps.
#1) Find the length of LCS of input string and its reverse. Let the length be ‘l’.
#2) The minimum number insertions needed is length of input string minus ‘l’.

def find_min_insertions_using_lcs(string):
    from longest_common_subsequence import lcs
    string_rev = ""
    string_rev = string[::-1]
    
    lcs = lcs(string, string_rev)
    #print lcs
    
    return len(string) - lcs


if __name__ == "__main__":
    print find_min_insertions_palin("abcd")
    print find_min_insertions_using_lcs("abcd")