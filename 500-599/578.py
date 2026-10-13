t = int(input())
for values in range(t):
    p,q,r,s = map(int,input().split())
    if p == q == r == s:
        print("NO")
    elif p +q + r < s or p+q+s < r or p+s+r < q or s+q+r < p:
        print("YES")
    else:
        print("NO")