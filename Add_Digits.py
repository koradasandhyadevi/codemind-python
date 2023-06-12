def add(n):
    while n > 9:
        n = (n % 10)+(n // 10)
    return n
n = int(input())
x = add(n)
print(x)