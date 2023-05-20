n = int(input())
l = list(map(int,input().split()))
s = 0
s1 = 0
for i in range(len(l)):
    if i%2==0:
        s+=l[i]
for i in range(len(l)):
    if i%2==1:
        s1+=l[i]
diff = abs(s - s1)
print(diff)