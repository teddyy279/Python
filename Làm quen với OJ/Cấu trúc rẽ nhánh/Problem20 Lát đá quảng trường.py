int n, m, a = map(int, input())
if(n % a == 0):
    tmp1 = n // a
else: tmp1 = n // a + 1
if(m % a == 0):
    tmp2 = m // a
else: tmp2 = m // a + 1
print(tmp1 * tmp2)