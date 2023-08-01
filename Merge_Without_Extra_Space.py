n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    x = l1+l2
    x.sort()
    print(*x)