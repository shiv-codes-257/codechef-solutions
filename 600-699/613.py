t = int(input())
for values in range(t):
    n,x = map(int,input().split())
    if x >= n and x % n == 0:
        print("YES")
    else:
        print("NO")