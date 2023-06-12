n = int(input())
l = list(map(int,input().split()))
c = 0
for i in l :
    x = str(i)
    y = x[::-1]
    if y == x:
        c+=1
print(c)