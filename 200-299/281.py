t = int(input())
for values in range(t):
    a,b = map(int, input().split())
    if a < b :
        print("B")
    else:
        print("A")