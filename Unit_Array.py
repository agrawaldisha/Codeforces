for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    su=sum(lst)
    cn=lst.count(-1)
    p=(-1)**cn
    ans=0
    while(p!=1 or su<0):
        cn-=1
        p=(-1)**cn
        su+=2
        ans+=1
    print(ans)
