n = int(input())
l = list(map(int,input().split()))
s = []
for i in l:
    x = l.count(i)
    if x == i:
        if i in s:
            pass
        else:
            s.append(i)
        
if len(s) == 0:
    print(-1)
else:
    print(*s)