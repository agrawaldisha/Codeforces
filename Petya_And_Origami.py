import math
n,k=map(int,input().split())
#2-red,5-blue,8-green
red=math.ceil((2*n)/k)
blue=math.ceil((5*n)/k)
green=math.ceil((8*n)/k)
print(red+green+blue)

