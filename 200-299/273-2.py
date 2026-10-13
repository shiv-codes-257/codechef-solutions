t= int(input())
for values in range(t):
    a,b = map(int,input().split())
    people_not= a-b
    if people_not < 0 :
        print("0")
    else:
        print(str(people_not))