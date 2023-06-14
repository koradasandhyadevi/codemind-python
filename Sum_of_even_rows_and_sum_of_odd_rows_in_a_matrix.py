r,c = map(int,input().split())
m = []
for i in range(r):
    l = list(map(int,input().split()))
    m.append(l)
c = 0
x = 0
for i in range(len(m)):
    if i % 2 == 0:
        for j in m[i]:
            c = c + j
    else:
        for j in m[i]:
            x = x + j
print(c,x)
    