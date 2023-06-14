n = input()
l = list(map(int,input().split()))
c = 0
x = 0
for i in l:
    if i % 2:
        c+=1
    else:
        x+=1
print(x,c)