t = int(input())
for values in range(t):
    a,b= map(int,input().split())
    score = int((a/10)*b)
    print(str(score))