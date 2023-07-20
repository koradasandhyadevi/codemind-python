n = int(input())
l = list(map(int,input().split()))
s = []
for i in range(n):
    if l[i] % 2 == 0:
        s.append(i)
print(s[-1])
        