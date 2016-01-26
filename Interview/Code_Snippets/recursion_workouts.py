import sys
import os

def Factorial(no):
    if no == 1:
        #print "calling recursin for no = ", no
        return 1
    else:
        #print "calling recursion for no = ", no
        return no * Factorial(no-1)


def main():
    print "calling recursion"
    no = input("enter a no for finding factorial of it : ")
    print "factorial of %d = %d" %(no,Factorial(no))

if __name__ == "__main__":
    sys.exit(main())