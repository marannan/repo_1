import sys
import os



def main():

    with open("US_States.txt", mode='r') as states_list_file:
        for line in states_list_file:
            word1, word2 = str(line).split("\t", 1)
            print "'" + str(word2).replace("\n","") + "'" + ":" + "'" + str(word1) + "'" + ","
    return
    

if __name__ == "__main__":
    main()