n = int(input())
x= 0
for values in range(n):
    user_input = input()
    if user_input == "++X" or user_input == "X++":
        x+=1
    elif user_input == "--X" or user_input == "X--": 
        x-=1
print(x)
    

    #strip removes any whitespaces before or after the input or a text for eg "hello world        " 
    #printing hello

    #removed for i in range(n):