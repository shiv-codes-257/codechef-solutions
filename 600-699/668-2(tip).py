import math

t = int(input())
for values in range(t):
    n = int(input())
    if math.sqrt(n).is_integer():
        print(int((math.sqrt(n))))
    else:
        print(int((math.sqrt(n-1) )))

        #learnt how to use import math and get a square root of a number using the math.sqrt function
        
        #and learnt how to use .is_integer() function. it checks whether a number is a whole number or not.