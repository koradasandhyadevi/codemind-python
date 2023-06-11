def is_prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c+=1
    if c == 2:
        return 0
    else:
        return 1
n = int(input())
l = list(map(int,input().split()))
s = []
y = []
for i in l :
    x = is_prime(i)
    if x == True:
        s.append(i)
    else:
        y.append(i)
p = 1
for i in s:
    p = p * i
b = 1
for i in y:
    b = b * i
print(abs(p-b))