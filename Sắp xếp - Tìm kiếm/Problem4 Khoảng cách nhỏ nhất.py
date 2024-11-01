if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  min_val = 10 ** 9 + 5
  for i in range(1, len(a)):
    if(a[i] - a[i - 1] < min_val):
      min_val = a[i] - a[i - 1]
  print(min_val)
  
