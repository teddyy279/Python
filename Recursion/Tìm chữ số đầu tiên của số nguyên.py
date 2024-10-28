def print_first_number(n):
    if(n > 10):
        print_first_number(n // 10)
    else: print(n)

if __name__ == '__main__':
    n = int(input())
    print_first_number(n)
