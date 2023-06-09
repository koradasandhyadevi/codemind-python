import math
n = int(input())
temp = n
x = int(math.log10(n) + 1)
s = 0
while(n > 0):
    d = n % 10
    s = s + pow(d,x)
    x-=1
    n = n // 10
if s == temp:
    print("True")
else:
    print("False")