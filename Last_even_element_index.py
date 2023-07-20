n = int(input())
l = list(map(int,input().split()))
s = []
for i in l:
    if i % 2 == 0:
        s.append(l.index(i))
print(s)
        