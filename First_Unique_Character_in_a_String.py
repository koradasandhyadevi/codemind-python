s = input()
l = []
for i in s:
    x = s.count(i)
    if x == 1:
        l.append(i)
if len(l) == 0:
    print(-1)
else:
    print(s.find(l[0]))
        
        