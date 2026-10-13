t = int(input())
for values in range(t):
    x,y,z = map(int,input().split())
    if x <= 3:
        print(x*y)
    elif x > 3:
        print((x*y) + (((x-1)//3)*z))

        #check later 

        #right answer

        #i guess the more problems you do the better ur logical thinking becomes.