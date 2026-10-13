t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    if y <= x+(x*7/100):
        print("YES")
    else:
        print("NO")

        #percentage- 107/100 = 7% as 107-100, have to read the wording and english properly and use logic properly as well.