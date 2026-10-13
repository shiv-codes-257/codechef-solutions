t= int(input())
for values in range(t):
    x,y = map(int,input().split())
    if (x*100) >= (y*10):
        print("Cloth")
    elif (x*100) < (y*10):
        print("Disposable") 
    elif x*100 == y*10:
        print("Cloth")