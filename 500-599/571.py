t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if x > y :
        print("CAR")
    elif x < y:
        print("BIKE")
    elif x == y:
        print("SAME")