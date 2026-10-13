t = int(input())
for values in range(t):
    a,b = map(int,input().split())
    if a/0.10 > b/0.20:
        print("FIRST")
    elif a/0.10 < b/0.20:
        print("SECOND")
    elif a/0.10 == b/0.20:
        print("ANY")