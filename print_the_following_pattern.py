n = int(input())
y = 65
for i in range(n):
    x = chr(y)
    y+=1
    for j in range(n):
        print(x,end=' ')
    print()