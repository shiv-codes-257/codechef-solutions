t = int(input())
for values in range(t):
    n= int(input())
    if (50*n)-((50*n)*0.7) < 0:
        print("0")
    else:
        print(int(((50*n)-((50*n)*0.7))))