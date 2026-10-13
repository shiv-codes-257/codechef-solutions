t = int(input())
for values in range(t):
    n,x = map(int,input().split())
    if n == x or n < x:
        print("YES")
    else:
        print("NO")