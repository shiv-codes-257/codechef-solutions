x,y = input().split()
x = int(x)
y = float(y)
if x % 5 != 0:
    print(y)
elif (y-x)-0.5 < 0:
    print(f"{y:.2f}")
elif x % 5 == 0 and x < y and (y-x)-0.5 >= 0:
    print(f"{(y-x)-0.5:.2f}")
elif x > y:
    print(y)

    #IF u want to print the difference is negative , the type if diff < 0 !!
    # diff < 0 
    # diff < 0
    # diff < 0