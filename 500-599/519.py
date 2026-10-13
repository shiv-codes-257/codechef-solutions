t = int(input())
for values in range(t):
    x,y,z = map(int,input().split())
    if z > (x*y)*0.5:
        print("YES")
    else:
        print("NO")