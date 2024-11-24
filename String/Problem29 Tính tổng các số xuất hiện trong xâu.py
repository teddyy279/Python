if __name__ == '__main__':
    s = input()
    t = ''
    for i in range(len(s)):
        if s[i].isalpha():
            t += ' '
        else:
            t += s[i]
    a = t.split()
    print(a)
    result = 0 
    for i in range(len(a)):
        result += int(a[i])
    print(result)
