for _ in range(int(input())):
    a,b=map(int,input().split())
    #print(((24-a)*60)+(60-b))
    print(((24*60)-((a*60+b))))
