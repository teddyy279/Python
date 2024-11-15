if __name__ == '__main__':
    s = input()
    s = s.lower()
    count = 0
    d = [0] * 26
    for i in range(len(s)):
        d[ord(s[i]) - ord('a')] = 1
    check = 1
    for i in range(26):
        if d[i] != 1:
            check = 0
            break
    if check: 
        print("YES")
    else:
        print("NO")
