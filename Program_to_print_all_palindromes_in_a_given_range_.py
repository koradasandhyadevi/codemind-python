def pal(n):
    x = str(n)
    y = x[::-1]
    if x == y:
        return 1
a = int(input())
b = int(input())
for i in range(a,b+1):
    z = pal(i)
    if z == 1:
        print(i,end = ' ')