t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if x == y:
        print("ANY")
    elif x < y:
        print("FIRST")
    elif x > y:
        print("SECOND")