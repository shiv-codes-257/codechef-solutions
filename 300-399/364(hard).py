t = int(input())
for values in range(t):
    x,y= map(int, input().split())
    if x > y:
        print("YES")
    else:
        print("NO")

        #it said which has more time complexity , basically which took more time, so if A has more sorts then A has more time complexity