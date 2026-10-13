t = int(input())
for values in range(t):
    n,k,m = map(int,input().split())
    print((n+((k*m)-1))//(k*m))


    #brackets are very important when doing calculation question and the operation symbols as well, either get the brackets right or store them as variables and then put them into the equation to get the answer, they might get a bit too confusing sometimes.

    #and also remember that to ROUND UP, you subtract -1 to what your dividing the number by and add it to the numerator.
    #and to ROUND DOWN u add +1