n=7
c=0
for i in range(0,n+1):
    for j in range(n,i,-1):
        print(j*2,end=" ")
    for k in range(0,c):
        print("  ",end=" ")
    for m in range(i+1,n+1):
        print(m*2,end=" ")
    print()
    c+=2
    
        
