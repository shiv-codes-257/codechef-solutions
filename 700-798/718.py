t = int(input())
for value in range(t):
    a,x,b,y = map(int,input().split())
    speed_alice = a/x
    speed_bob = b/y
    if speed_alice > speed_bob:
        print("Alice")
    elif speed_bob > speed_alice:
        print("Bob")
    else:
        print("Equal")