import math
n = input()
l = list(map(int,input().split()))
y = []
for i in l:
    x = int(math.sqrt(i))
    if x*x == i:
        y.append(i)
print(sum(y))
    