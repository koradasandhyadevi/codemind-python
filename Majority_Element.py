n = int(input())
l = list(map(int,input().split()))
s = []
for i in l:
    x = l.count(i)
    s.append(x)
y = s.index(max(s))
print(l[y])