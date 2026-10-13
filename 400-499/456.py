t = int(input())
for values in range(t):
    x, y = map(int,input().split())
    if (y*30) > x:
        print("NO")
    elif (y*30 ) <= x:
        print("YES")