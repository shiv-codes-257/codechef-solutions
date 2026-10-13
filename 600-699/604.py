t = int(input())
for values in range(t):
    n,x   = map(int,input().split())
    y = list(map(int,input().split()))
    count = 0
    for i in y:
        if i >= x:
            count += 1
    print(count)
