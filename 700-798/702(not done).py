t = int(input())
for values in range(t):
    s,x,y,z = map(int,input().split())
    app_storage = x+y
    if z < (s-(app_storage)):
        print("0")
    elif z == s-app_storage:
        print((z+(x+y+1))//(x+y))
    elif z > s-app_storage:
        print(z+(x+y-1)//(x+y))


        #dont understand