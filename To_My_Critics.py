    test=int(input())
    for j in range(test):
        x,y,z=map(int,input().split())
        if(x+y>=10 or y+z>=10 or z+x>=10):
            print("YES")
        else:
            print("NO")
