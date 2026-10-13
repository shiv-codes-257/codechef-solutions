t = int(input())
for values in range(t):
    x = int(input())
    if x % 10 == 0:
        print(int((x/10)))
    elif x % 5 == 0 and x % 10 != 0:
        print(int((((x-5)/10) + 1 )))
    else:
        print("-1")
        #hard

        #dont overcomplicate things!!!