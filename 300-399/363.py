t = int(input())
for values in range(t):
    n,x,k = map(int,input().split())
    if (n*x) <= k:
        print("YES")
    else:
        print("NO")