for _ in range(int(input())):
    l,b,z=list(map(int, input().split()))
    c=(b+1)//2 - l//2
    if z>=c or (l==b and l>1):
        print("YES")
    else:
        print("NO")
