t = int(input())
for values in range(t):
    a,b,c,d = map(int,input().split())
    print(max(a,b)+max(c,d))