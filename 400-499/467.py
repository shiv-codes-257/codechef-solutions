count = 0
p1,p2,p3,p4 = map(int,input().split())
if p1 >= 10:
    count +=1
elif p1 >=10 and p2 >= 10:
    count +=2
elif p3 >= 10:
    count +=1
elif p4 >= 10:
    count +=1
print(count)