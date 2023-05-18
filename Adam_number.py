n = int(input())
sq = n*n
rev = 0
rev1 = 0
while(n):
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
sq1 = rev * rev
while(sq1):
    q = sq1 % 10
    rev1 = rev1 * 10 + q
    sq1 = sq1 // 10
if sq == rev1:
    print('True')
else:
    print('False')
    