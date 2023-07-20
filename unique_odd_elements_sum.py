n = int(input())
l = list(map(int,input().split()))
x = set(l)
s = []
for i in x:
    if i % 2 == 1:
        s.append(i)
print(sum(s))