n = int(input())
l = list(map(int,input().split()))
s = []
for i in l:
    x = l.count(i)
    if x == i:
        s.append(i)
if len(s) == 0:
    print(-1)
else:
    y =  set(s)
    print(min(y),max(y))