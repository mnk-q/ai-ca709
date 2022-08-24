from math import gcd
for t in range(int(input())):
    a,b,c,d = map(int, input().split())
    u = a/b
    v = c/d
    if u == v :
        print(0)
        continue
    if u == 0 or v==0:
        print(1)
        continue
    

    