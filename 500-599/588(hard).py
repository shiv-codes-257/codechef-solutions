t = int(input())
for values in range(t):
    n = int(input())
    print(int(str(n)[::-1]))


    # to reverse anything or user input we use [::-1], we do -1 since it is from backwards
    # to use [::-1], it has to be an input, it can be int , it has to be a string input or just an input
    #if your input is an integer, you convert it into a string, reverse it ,and the convert it back to an integer
    # while converting to str and back to integer the input and the [::-1], need to be in different brackets