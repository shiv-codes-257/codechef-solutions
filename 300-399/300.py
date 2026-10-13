n = int(input())
for values in range(n):
    x,y,z = map(int,input().split())
    print(sorted([x,y,z])[1])

# we could also do this asw - the one below 

n = int(input())
for values in range(n):
    x,y,z = map(int,input().split())
    if x<y<z or z<y<x:
        print(y)
    elif y<x<z or z<x<y:
        print(x)
    elif x<z<y or y<z<x:
        print(z)
    