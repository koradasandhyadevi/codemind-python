n = int(input())
l = list(map(int,input().split()))
se = int(input())
c = 0
for i in l:
    if i == se:
        c+=1
        break
if c == 1:
    print("True")
else:
    print('False')