t = int(input())
for values in range(t):
    n,x = map(int,input().split())
    if (n-x) > x:
        print("NO")
    else:
        print("YES")