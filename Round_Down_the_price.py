for _ in range(int(input())):
    t=int(input())
    x=t
    count=0
    while(t>0):
        count+=1
        t//=10
    #print(count)
    power=pow(10,count-1)
    #print(power)
    print(abs(power-x))
