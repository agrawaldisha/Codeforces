n=int(input())
s=(input()).lower()
lst=list(set(s))
if(len(lst)==26):
    print("YES")
else:
    print("NO")
    
