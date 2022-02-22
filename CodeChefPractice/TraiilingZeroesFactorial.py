t=int(input())
l=[]
for i in range(t):
    a=int(input())
    l.append(a)
    
    ts=f=0
    
    a=l[-1]
    while(a>4):
        a=a//5
        f=f+a
    
    print(f)
