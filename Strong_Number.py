n = int(input())
temp = n
s = 0
while(n):
    f = 1
    d = n % 10
    for i in range(d,0,-1):
        f = f * i
    s = s + f
    n = n // 10
if s == temp:
    print(f'The number {temp} is a strong number')
else:
    print(f'The number {temp} is not a strong number')