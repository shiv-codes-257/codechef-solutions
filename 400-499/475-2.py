t = int(input())
for values in range(t):
    x,y,z = map(int,input().split())
    if x*10 >= y:
        print(y*z)
    elif x*10 < y:
        print((x*10)*z)
    