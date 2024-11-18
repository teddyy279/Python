if __name__ == '__main__':
    s = input()
    a = 'python'
    index = 0
    for x in s:
        if x == a[index]:
            index += 1
        if index == 6:
            print("YES")
            exit()
    print("NO")
