I=input
for _ in[0]*int(I()):
 n,d=I().split();s=I();i=0
 while i<len(s)and s[i]>=d:i+=1
 print(s[:i]+d+s[i:])
