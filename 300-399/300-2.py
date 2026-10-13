t = int(input())
for values in range(t):
    x,y = map(int, input().split())
    if x < y:
        print("PROFIT")
    elif x > y:
        print("LOSS")
    elif x == y:
        print("NEUTRAL")