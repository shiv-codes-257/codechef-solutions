t = int(input())
for values in range(t):
    x,y =map(int,input().split())
    if x*3 <= y*2:
        print(x*3)
    elif y*2 <= x*3:
        print(y*2)