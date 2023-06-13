n = int(input())
l = list(map(int,input().split()))
for i in l:
        if i % 2 == 1:
            x = l.index(i)
            break
s = 0
for i in range(x):
    s = s + l[i]
print(s)