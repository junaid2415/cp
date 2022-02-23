# problem : "https://www.codechef.com/problems/HORSES"
# codechef practice easy 

t=int(input())
l=[]
for i in range(t):
    a=int(input())
    s=list(map(int, input().split()))
    s.sort();
    
    d=abs(s[0]-s[1])
    for i in range(1,a):
        if(d > abs(s[i]-s[i-1])):
            d = abs(s[i]-s[i-1])
    print(d)