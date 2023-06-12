n = int(input())
l = list(map(int,input().split()))
k = int(input())
x = l.index(k)
s = 0
for i in range(x+1):
    s = s + l[i]
print(s)