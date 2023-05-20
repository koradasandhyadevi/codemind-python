n = int(input())
l = list(map(int,input().split()))
s = 0
s1 = 0
for i in l:
    if i % 2 == 0:
        s+=i
    else:
        s1+=i
diff = abs(s - s1)
print(diff)