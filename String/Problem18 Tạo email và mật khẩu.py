if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        a = s.split()
        email = ''
        birth_of_date = a[-1]
        email += a[-2].lower()
        for i in range(len(a) - 2):
            a[i] = a[i].lower()
            email += a[i][0]
        email += '@xyz.edu.vn'
        print(email)
        password = birth_of_date.split('/')
        for i in range(len(password)):
            print(int(password[i]), end='')
