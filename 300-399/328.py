t = int(input())
for values in range(t):
    x = int(input())
    if x < 3:
        print("Light")
    elif 3<=x<7:
        print("Moderate")
    elif  x >= 7:
        print("Heavy")
        