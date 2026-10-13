t = int(input())
for values in range(t):
    a,b = map(int,input().split())#
    x = 21-(a+b)
    if x > 10:
        print("-1")
    elif 1<=x<=10:
        print(x)