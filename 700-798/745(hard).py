t = int(input())
for values in range(t):
    x,y,a,b = map(int,input().split())
    if x == a and y == b or y == a and x == b:
        print("0")
    elif x != a and x!=b and y!=a and y!=b:
        print("2")
    elif x != a and y == b or x == a or y!=b:
        print("1")

        #u could have used set function to remove any duplicates from the values and then -2

        #the goal is to understand the question, and get the answer in a simple way.

        #learnt set and len