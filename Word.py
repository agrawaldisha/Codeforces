n=input()
l=0
u=0
for i in n:
    if(i.isupper()==True):
        u+=1
    else:
        l+=1
if(u>l):
    print(n.upper())
else:
    print(n.lower())
