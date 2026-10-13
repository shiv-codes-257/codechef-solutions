t = int(input())
for values in range(t):
    x,y,z= map(int,input().split())
    print((x-y)+z)

    #dont need to use str to do calculations, python automatically converts them to strings while doing math