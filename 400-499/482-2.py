t = int(input())
for values in range(t):
    r1, r2, r3 = map(int,input().split())
    if r1 > r2+r3 or r2 > r1+r3 or r3> r1+r2:
        print("Yes")
    elif r1 == r2+ r3 or r1 < r2+r3:
        print("NO")
    elif r2 == r1+r3 or r2 < r1 + r3:
        print("NO")
    elif r3 == r1+r2 or r3 < r1+r2:
        print("NO")