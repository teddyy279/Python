if __name__ == '__main__':
    s1 = input()
    s2 = input()
    d1 = dict({})
    d2 = dict({})
    
    for x in s1:
        d1[x] = 1
    for x in s2:
        d2[x] = 1
    
    for x in sorted(s1):
      if x in d1 and x in d2:
        print(x, end = ' ')
        d1.pop(x)
    print()
    t = list(s1 + s2)
    t.sort()
    print(''.join(t))
