t = int(input())
for values in range(t):
    x,y,z = map(int,input().split())
    if (z-(y//x)) <= 0:
        print("0")
    else:
        print(z-(y//x))