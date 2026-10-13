import math

t = int(input())
for values in range(t):
    x,n = map(int,input().split())
    num_of_planes = math.ceil(n/100)
    if num_of_planes-x < 0:
        print("0")
    else:
        print(num_of_planes-x)
    
    







    #to round up we the ((denominator -1)) , for eg. if we want to round up , either we use ceil or (n+100-1)//100

    #to use math.ceil, we just do normal division inside the math.ceil() function