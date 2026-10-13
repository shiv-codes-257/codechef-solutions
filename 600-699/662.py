t = int(input())
for values in range(t):
    n,x,k = map(int,input().split())
    print(min(k//x,n))