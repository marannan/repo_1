def reverse(num):
    rev = 0
    while(num > 0):
        rev = (10*rev)+num%10
        num //= 10
    return rev

if __name__ == "__main__":
    print reverse(1234)
