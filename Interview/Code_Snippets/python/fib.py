__author__ = 'Ashok Marannan'

import sys
import os

def fib_recurse(no):
    if no <= 1:
        return no
    else:
        return (fib_recurse(no-1) + fib_recurse(no-2))


def fib_iterative(n):
    first = 0
    second = 1
    
    
    for i in range(n):
        third  = first + second
        second = first
        first = third
    
    return first

if __name__ == "__main__":
    print fib_recurse(10)
    print fib_iterative(10)


