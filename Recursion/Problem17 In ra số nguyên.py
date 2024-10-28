def print1(n):
    if(n != 0):
        print1(n // 10)
        print(n % 10, end = ' ')

def print2(n):
    if(n != 0):
        print(n % 10, end = ' ')
        print2(n // 10)

if __name__ == '__main__':
    n = int(input())
    print1(n)
    print()    
    print2(n)
