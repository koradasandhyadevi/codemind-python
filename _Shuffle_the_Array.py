n = int(input())
l = list(map(int,input().split()))
x = int(input())
a = []
b = []
for i in range(x):
    a.append(l[i])
for i in range(x,len(l)):
    b.append(l[i])
l = []
for i in range(x):
    l.append(a[i])
    l.append(b[i])
print(*l)