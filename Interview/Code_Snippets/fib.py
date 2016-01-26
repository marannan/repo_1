__author__ = 'Ashok Marannan'

import sys
import os

def Fibonacci(no):
    if no <= 1:
        return no
    else:
        return (Fibonacci(no-1) + Fibonacci(no-2))

def main():
    print "fibonacci"


    no = 10#input("Enter no to print fibonacci series until the no : ")
    for i in range(100):
        if Fibonacci(i) <= no:
            print Fibonacci(i)
        else:
            sys.exit()


if __name__ == "__main__":
    main()


