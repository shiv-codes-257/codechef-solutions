t = int(input())
for values in range(t):
    na,nb,nc = map(int,input().split())
    if na> nb+nc or nb> na+nc or nc > na+nb:
        print("YES")
    elif na <= nb+nc or nb <= na+nc or nc <= na+nb:
        print("NO")