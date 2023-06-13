a,b = map(int,input().split())
l = list(map(int,input().split()))
l1 = list(map(int,input().split()))
s = [ ]
for i in l:
    if i not in l1:
        s.append(i)
for j in l1:
    if j not in l:
        s.append(j)
print(*s)