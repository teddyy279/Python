def check(s):
    tmp = s[::-1]
    return tmp == s and '6' in s

if __name__ == '__main__':
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
