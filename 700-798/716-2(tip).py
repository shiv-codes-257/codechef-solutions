t = int(input())
for values in range(t):
    x,y,d = map(int,input().split())
    if abs(x-y) <= d:
        print("YES")
    else:
        print("NO")

        #range matter always, check range or constraints if doubt about solution