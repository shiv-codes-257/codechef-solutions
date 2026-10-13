t = int(input())
for values in range(t):
    x = int(input())
    if x % 10 == 0:
        print("0")
    elif x < 10:
        print(x*1)
    elif x % 10 !=0:
        print(x-((x//10)*10))