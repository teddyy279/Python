if __name__ == '__main__':
    name = input()
    words = name.split()
    date_of_birth = input()
    print(' '.join(words))
    if date_of_birth[1] == '/':
        date_of_birth = '0' + date_of_birth
    if date_of_birth[4] == '/':
        date_of_birth = date_of_birth[0: 3] + '0' + date_of_birth[3:]
    print(date_of_birth)
