t = int(input())
for values in range(t):
    w,x,y,z = map(int,input().split())
    if w+(y*z) > x:
        print("Overflow")
    elif w+(y*z) < x:
        print("Unfilled")
    elif w+(y*z) == x:
        print("Filled")