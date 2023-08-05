n=int(input())
ans=False
lst=list(map(int,input().split()))
for i in lst:
    if(i==1):
        ans=True
        break
if(ans==True):
    print("HARD")
else:
    print("EASY")
