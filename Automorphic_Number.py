n = int(input())
sq = n * n
s = str(n)
q = str(sq)
if q.endswith(s):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")