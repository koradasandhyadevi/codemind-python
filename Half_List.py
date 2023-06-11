n = int(input())
l = list(map(int,input().split()))
x = n//2
s = []
for i in l[x:]:
    s.append(i)
y = s[::-1]
for i in l[0:x]:
    y.append(i)
print(*y)