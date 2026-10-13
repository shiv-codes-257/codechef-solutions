t = int(input())
for values in range(t):
    a,b,x,y = map(int,input().split())
    if x*y >= a*b:
        print("YES")
    else:
        print("NO")