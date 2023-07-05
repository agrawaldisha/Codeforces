#gives tle in codeforces
for _ in range(int(input())):
    n=int(input())
    count=0
    for i in range(1,n+1):
        ans=0
        while(i>0):
            #print(i)
            r=i%10
            if(r!=0):
                ans+=1
            i=i//10
        if(ans==1):
            count+=1
    print(count)
