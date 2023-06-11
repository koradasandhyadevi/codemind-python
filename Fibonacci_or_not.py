n = int(input())
a = 0
b = 1
l = []
for i in range(n*n):
    l.append(a)
    c = a+b
    a = b
    b = c
if n in l:
    print('True')
else:
    print('False')