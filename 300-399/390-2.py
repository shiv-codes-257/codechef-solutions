t = int(input())
for values in range(t):
    x = int(input())
    if x <4:
        print("Mild")
    elif 4<=x<7:
        print("Medium")
    elif x>= 7:
        print("Hot")