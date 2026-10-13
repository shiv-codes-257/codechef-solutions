t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if y >= x*0.5:
        print("YES")
    else:
        print("NO")