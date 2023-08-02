import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    x=((b*math.ceil(c/b*1.0))+a)
    print(x," ",b," ",c)
