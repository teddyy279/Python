if __name__ == '__main__':
    s = input()
    alpha, digit, special = 0, 0, 0
    for x in s:
        if x.isdigit():
            digit += 1
        elif x.isalpha():
            alpha += 1
        else:
            special += 1
    print(alpha, digit, special)
