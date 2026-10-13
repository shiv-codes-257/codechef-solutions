t = int(input())
for values in range(t):
    n,x = map(int,input().split())
    y = n-x
    if x < y:
        print(x)
    elif y < x:
        print(y)
    elif n == x:
        print("0")
    elif x == y:
        print(x)

        #check solution
        
        #if ur making new variables, thoroughly check if your variables that u put in ur code or if statements are correct, as they can mess up your answer, and try to enter all edgecases in if and elif statements, as theres lesser risk of statements.

        #right answer