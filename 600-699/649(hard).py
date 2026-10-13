t = int(input())
for values in range(t):
    x = int(input())
    if x % 3 == 0:
        print("NORMAL")
    elif x % 3 == 1:
        print("HUGE")
    else:
        print("SMALL")

        # need to think of how to get the answer, not every answer is in loop, and loop isnt required everyhwere, just need to get the answer,answer