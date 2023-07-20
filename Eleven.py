n=int(input())
a=0
b=1
#print("O",end="")
for i in range(1,n+1):
    c=a+b
    if(c==i):
        a=b
        b=c
        print("O",end="")
    else:
        print("o",end="")
    
