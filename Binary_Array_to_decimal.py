n = int(input())
l = list(map(int,input().split()))
x = 0
p = len(l) - 1
for i in l:
    if i == 1:
        x += 1 << p
        p-=1
    else:
        p-=1
print(x)
        