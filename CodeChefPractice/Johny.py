# problem link = "https://www.codechef.com/problems/JOHNY"

t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int, input().split()))
    k=int(input())
    a=s[k-1]
    s.sort();
    print(s.index(a)+1)
    
    