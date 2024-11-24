def is_divisible_4(s):
    if len(s) > 1:
        return int(s[-2::]) % 4 == 0
    else:
        return int(s[-1]) % 4 == 0

if __name__ == '__main__':
    s = input()
    if is_divisible_4(s):
        print("YES")
    else:
        print("N0")
