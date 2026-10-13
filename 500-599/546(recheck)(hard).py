t = int(input())
for values in range(t):
    n,x = map(int,input().split())
    print((n*x+3)//4)
  
        #check solution later
        #what u have to do is to round it to such a number that rounds the number up instead of down , //4 , rounds the number down, so we add (a*b-1)//4 , and thats why we add 3 to the product. we can also use ceil function using import math 