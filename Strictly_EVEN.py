n = int(input())
l = list(map(int,input().split()))
c = 0
s = []
for i in range(n):
    if l[i] % 2 == 0:
        s.append(l[i])
        if i % 2 == 0:
            c+=1
if c == len(s):
    print('True')
else:
    print('False')
    