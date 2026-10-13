t  = int(input())
for values in range(t):
    n,x,p = map(int,input().split())
    incorrect_questions = n-x
    correct_marks = x*3
    incorrect_marks = incorrect_questions*-1
    total_marks = correct_marks+incorrect_marks
    if total_marks >= p:
        print("PASS")
    else:
        print("FAIL")
