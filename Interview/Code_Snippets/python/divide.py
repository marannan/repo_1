def divide(dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)


def divide_2(dividend, divisor):     
    neg=( (dividend < 0) != (divisor < 0) )
    dividend = left = abs(dividend)
    divisor  = div  = abs(divisor)
    Q = 1
    ans = 0
    while left >= divisor:
        left -= div
        ans  += Q 
        Q    += Q
        div  += div
        if left < div:
            div = divisor
            Q = 1
    if neg:
        return max(-ans, -2147483648)
    else:
        return min(ans, 2147483647)
    

if __name__ == "__main__":
    print divide_2(10,5)