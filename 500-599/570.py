
t = int(input())
for values in range(t):
    n,x = map(int,input().split())
    if x > n :
        print("0")
    else:
        print(((n-x)+3)//4 )

        #dont know why the ceiling trick of rounding the number wasnt working before, but logic effort was decent now, got a bit confused but i think i understand the ceiling trick just -1 by the number your dividing it with.