t = int(input())
for values in range(t):
    a,b,c,x = map(int,input().split())
    if a+b >= x or a + c >= x or b+a >= x or b+c >= x or c+a >=x or c+b >= x:
        print("YES")
    else:
        print("NO")

        # shortcuts are not good or neccessary . they are good for saving time, but only use them if you are sure they are going to work , for e.g a+b >= x or a+c >= x, and u pressed , but u forgot about b’s variation.