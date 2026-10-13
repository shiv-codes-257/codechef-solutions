t = int(input())
for values in range(t):
    n,m,k = map(int,input().split())
    if n > m-k:
        print("NO")
    elif n <= m-k:
        print("YES")