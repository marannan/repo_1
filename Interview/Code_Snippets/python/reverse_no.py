def reverse(num):
    rev = 0
    sign  = 1
    if num < 0:
        sign = -1
        num = num * sign
    while(num > 0):
        rev = (10*rev)+num%10
        num //= 10

    return rev * sign

if __name__ == "__main__":
    print reverse(-1234)
