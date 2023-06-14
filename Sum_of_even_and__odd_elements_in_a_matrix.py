r,c = map(int,input().split())
m = []
for i in range(r):
    l = list(map(int,input().split()))
    m.append(l)
c = 0
x = 0
for i in m:
    for j in i:
        if j % 2 == 0:
            c+=j
        else:
            x+=j
print(c,x)
    