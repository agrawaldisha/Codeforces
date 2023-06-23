t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print(max(0,max(b,c)+1-a),end=" ")
    print(max(0,max(a,c)+1-b),end=" ")
    print(max(0,max(a,b)+1-c))
    
