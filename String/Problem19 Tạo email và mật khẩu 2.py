if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        a = s.split()
        email = a[-2].lower()
        date_of_brith = a[-1]
        for i in range(len(a) - 2):
            a[i] = a[i].lower()
            email += a[i][0]
        email += '@xyz.edu.vn'
        print(email)
        password = date_of_brith.split('/')
        for i in range(len(password)):
            print(int(password[i]), end = '')
        print()
