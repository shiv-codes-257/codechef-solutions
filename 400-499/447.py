t = int(input())
for values in range(t):
    a,b,c,d = map(int,input().split())
    if a-c < b-d :
        print("First")
    elif a-c > b-d:
        print("Second")
    elif a-c == b-d:
        print("Any")
