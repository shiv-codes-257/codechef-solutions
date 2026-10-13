t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    print(((y-x)+7)//8)

    # need to know when to round up or down 