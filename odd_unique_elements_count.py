n = int(input())
l = list(map(int,input().split()))
x = set(l)
c = 0
for i in x:
    if i % 2 == 1:
        c+=1
print(c)