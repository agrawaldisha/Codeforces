y,bl=map(int,input().split())
a,b,c=map(int,input().split())
yc=a*2+b*1
bc=b*1+c*3
ans=0
if(yc>y):
    ans=ans+(yc-y)
if(bc>bl):
    ans=ans+(bc-bl)
print(ans)
