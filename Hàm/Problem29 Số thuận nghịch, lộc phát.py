from math import*

def check_palindrome_number(n):
    original = n
    res = 0
    cnt = 0
    while n != 0:
        tmp = n % 10
        if(tmp == 6): cnt = 1
        res = res * 10 + tmp
        n //= 10
    return original == res and cnt == 1

def sum_digit(n):
    sum1 = 0
    while n != 0:
        sum1 += n % 10
        n //= 10
    return sum1 % 10 == 8
    

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if(check_palindrome_number(i) and sum_digit(i)):
            print(i, end = ' ')
