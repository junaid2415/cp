problem link = "https://www.codechef.com/problems/CIELAB"


a,b = map(int, input().split())

d = a-b


if((d+1) % 10 == 0):
    print(d-1)
else:
    print(d+1)


