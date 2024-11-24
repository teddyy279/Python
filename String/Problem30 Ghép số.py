if __name__ == '__main__':
    s = input()
    t = ""
    for i in range(len(s)):
        if s[i].isalpha():
            t += ' '
        else:
            t += s[i]
    a = t.split()
    a.sort(key = lambda x : int(x))
    result = ''
    for i in range(len(a) - 1, - 1, - 1):
        result += a[i]
    print(result)
