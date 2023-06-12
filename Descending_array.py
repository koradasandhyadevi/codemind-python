n = int(input())
l = list(map(int,input().split()))
x = sorted(l)
z = x[::-1]
if z == l:
    print('yes')
else:
    print('no')