r,c = map(int,input().split())
m = []
for i in range(r):
    l = list(map(int,input().split()))
    m.append(l)
c = 0
for i in m:
    for j in i:
        c = c + j
print(c)
    