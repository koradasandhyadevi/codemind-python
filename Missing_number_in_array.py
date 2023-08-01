n = int(input())
for i in range(n):
    x = int(input())
    l = list(map(int,input().split()))
    s = []
    for i in range(1,x+1):
        s.append(i)
    for i in s:
        if i not in l:
            print(i)
