t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if y < x:
        print("0")
    else:
        print(str(y-x))