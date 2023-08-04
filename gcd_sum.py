import math
for _ in range(int(input())):
    n=int(input())
    while math.gcd(n,sum(map(int,list(str(n)))))==1:
        n+=1
    print(n)
