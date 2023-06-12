n = int(input())
l = list(map(int,input().split()))
s = []
for i in l:
    x = l.count(i)
    if x == i:
        s.append(i)
y = set(s)
print(len(y))