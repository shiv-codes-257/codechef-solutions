t = int(input())
for values in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in a:
        if 10<=i<=60:
            count += 1
    print(count)

    #when using a list , and wanting to make it into int, then u need to first define it as a list, then use map to define it as a integer, and then use input and split as normal