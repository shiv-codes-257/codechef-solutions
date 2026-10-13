t = int(input())
for values in range(t):
    x1, y1 ,x2 ,y2 = map(int,input().split())
    print(max(abs(x1-x2),abs((y1-y2))))


    # when using a function in brackets such as (abs) or something, especially for two numbers, we need to define it or use it for both numbers, reduces the chance of error.

    #learnt how to use abs() function - absolute value, no negative numbers even if the number is negative, only positive output.