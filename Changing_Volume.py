# gives TLE

for _ in range(int(input())):
    a,b=map(int,input().split())
    count=0
    while(a>b):
        if(a-b>=5):
            a=a-5
            count+=1
        elif(a-b>=2):
            a=a-2
            count+=1
        elif(a-b>=1):
            a=a-1
            count+=1
        #print(count,a)
    while(a<b):
        if(a<b):
            if(b-a>=5):
                a=a+5
                count+=1
            elif(b-a>=2):
                a=a+2
                count+=1
            elif(b-a>=1):
                a=a+1
                count+=1
        #print(count)
    print(count)
        
