if __name__ == '__main__':
    name = input()
    words = name.split()
    words[-1] = words[-1].upper()
    for i in range(0, len(words) - 1):
        words[i] = words[i].title()
    for i in range(0, len(words) - 1):
        if i != len(words) - 1:
            print(words[i], end = ' ')
        else:
            print(words[i], end = ', ')
    print(words[-1])
    print(words[-1], end = ', ')
    for i in range(0, len(words) - 1):
        print(words[i], end = ' ')

