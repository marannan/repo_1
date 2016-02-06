import sys
import os

def RecursivePrinting(no):
    if no == 0:
        return 0
    else:
        print no
        RecursivePrinting(no-1)

def main():
    print "recursive printing of no"
    RecursivePrinting(10)

if __name__ == "__main__":
    main()
