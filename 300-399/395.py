t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if (x*5) < y:
        print("NO")
    elif y <= (x*5):
        print("YES")