s = input()
z = s.split()
c = 0
for i in z:
    x = i.upper()
    y = x[::-1]
    if x == y:
        c+=1
print(c)