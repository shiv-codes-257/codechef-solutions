t = int(input())
for values in range(t):
    n = int(input())
    sum = 1
    for i in range(1,n+1 ):
        sum *= i
    print(sum)

    # we use the *= function to multiply a variable by the value of i
