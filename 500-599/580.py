t = int(input())
for values in range(t):
    n = int(input())
    d = list(map(int,input().split()))
    x = 0
    for i  in d:
        if i >= 1000:
            x+=1
    print(x)

    #watch out for silly mistakes