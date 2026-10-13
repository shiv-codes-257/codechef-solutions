t = int(input())
for values in range(t):
    x,y = map(int,input().split())
    whole_steps = x//y
    if x % y == 0:
        print(whole_steps)
    elif x%y != 0:
        print((whole_steps)+(x-(y*whole_steps)))


        #you cant just use print everytime and get the answer, if and else are still important

        #you cant just keep guessing the answer either, you need to attempt the question properly, and then try the inputs