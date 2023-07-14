import math;
t=int(input())
n=input()
l=['4','7']
ans=True
for i in n:
    if(i not in l):
        ans=False
        break
sum1=0
sum2=0
for i in range (0,(t//2)):
    sum1+=int(n[i])
for j in range(t//2,t):
    sum2+=int(n[j])
if(ans==True and sum1==sum2):
    print("YES")
else:
    print("NO")
