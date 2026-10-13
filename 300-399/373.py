t = int(input())
for values in range(t):
    x1, y1, x2, y2 = map(int,input().split())
    if x1+y1 <= x2+y2:
        print(x1+y1)
    elif (x2+y2) <= (x1+y1):
        print(x2+y2)

        #silly mistakes ?? 