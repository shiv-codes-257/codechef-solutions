t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if y <= x:
        print(y)
    elif y > x:
        print(x)

        #rebatable meaning?