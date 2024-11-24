def is_divisible_6(s):
    if int(s[-1]) % 6 != 0:
        return False
    sum_digit = 0
    for i in range(len(s)):
        sum_digit += int(s[i])
    if sum_digit % 3 != 0:
        return False
    return True

if __name__ == '__main__':
    s = input()
    if is_divisible_6(s):
        print("YES")
    else:
        print("NO")
