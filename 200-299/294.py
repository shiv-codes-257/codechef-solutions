t= int(input())
for values in range(t):
    x,y = map(int,input().split())
    if x == y or x > y:
        print("YES")
    else:
        print("NO")