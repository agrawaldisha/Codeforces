for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    cnt=lst.count(0)
    if(cnt==len(lst)):
        print(1)
    else:
        print(len(lst))
