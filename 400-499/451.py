t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if x < y:
        print("Repair")
    elif x > y:
        print("New phone")
    elif x == y:
        print("Any")