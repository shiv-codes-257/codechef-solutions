t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if x >y :
        print(str(x-y))   
    elif x <= y :
        print("0")