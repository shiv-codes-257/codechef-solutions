t = int(input())
for values in range(t):
    a,b,x,y = map(int,input().split())
    x = x/60
    y = y/60
    if a/x > b/y:
        print("Chefina")
    elif a/x < b/y:
        print("Chef")
    elif a/x == b/y:
        print("Both")