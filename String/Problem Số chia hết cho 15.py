def is_divisible_15(s):
    last_digit = s[-1]
    if last_digit not in '05':
        return False
    sum_digit = 0
    for i in range(len(s)):
        sum_digit += int(s[i])
    return sum_digit % 3 == 0

if __name__ == '__main__':
    s = input()
    if is_divisible_15(s):
        print("YES")
    else:
        print("N0")
