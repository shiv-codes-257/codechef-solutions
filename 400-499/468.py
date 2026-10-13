t = int(input())
for values in range(t):
    x,y,z = map(int,input().split())
    if (x*y) > (z*24*60):
        print("NO")
    elif (x*y) <= (z*24*60):
        print("YES")