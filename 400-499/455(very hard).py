t = int(input())
for values in range(t):
    n = int(input())
    sum = 0
    for j in str(n):
        sum += int(j)
    print(sum)

    # learnt += , it means to add and assign something for.eg x += 5 is x = x+5
    # can use more for loops ,can define a variable before for loop as well 
    # need to convert to int when adding something 