t = int(input())
for values in range(t):
    a,b,c = map(int,input().split())
    if max(a,c) <=b :
        print("YES")
    else:
        print("NO")
    

    #check later

    #so silly mistake while reading. need to read carefully so that we dont make mistakes or get confused while writing code

    #we used the max function in this case, as it says the temperature for A is greater than or equal to and the temp for C is greater than or equal to as well. so we use the max function to find the bigger temperature and then compare it to the temperature of B. if its lesser than B, then its fine, it cant be greater than B because of the condition given in the question.