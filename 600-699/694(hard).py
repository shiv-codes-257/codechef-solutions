t = int(input())
for values in range(t):
    a,b,x,y = map(int,input().split())
    temp_needed = abs(b-a)
    if a == b:
        print("YES")
    elif b > a and x >= temp_needed:
        print("YES")
    elif b < a and y >= temp_needed:
        print("YES")
    else:
        print("NO")

        #read question properly