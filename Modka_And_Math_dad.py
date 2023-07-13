for _ in range(int(input())):
    n=int(input())
    ans=""
    last=0
    if(n%3==1):
        last=2
    else:
        last=1
    while(n>0):
        last=3-last
        n=n-last
        ans=ans+str(last)
    print(ans)
        
