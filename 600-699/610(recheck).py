t = int(input())
for values in range(t):
    n,x,y = map(int,input().split())
    if n*x < y:
        print("NO")
    elif n*x > y:
        print("NO")
    elif n*x == y:
        print("YES")

        #check later