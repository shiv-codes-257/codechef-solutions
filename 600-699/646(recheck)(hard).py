t = int(input())
for values in range(t):
    n,m = map(int,input().split())
    total = n*2
    if n > m:
        print((n*2)-m)
    elif n < m:
        print((total)-(m//n))
    elif n == m:
        print((n*2)-m)

        #hard

        #recheck

        #wrong answer
    