t = int(input())
for values in range(t):
    a,b,c = map(int,input().split())
    sorted_nums = sorted([a,b,c])
    print(sorted_nums[1])


# to sort numbers it has to be a list