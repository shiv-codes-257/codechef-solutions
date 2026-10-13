t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if y > x:
        print("YES")
    else:
        print("NO")