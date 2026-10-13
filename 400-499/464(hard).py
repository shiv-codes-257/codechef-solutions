n,k = map(int,input().split())
count = 0
for values in range(n):
    x = int(input())
    if x % k == 0:
        count += 1
print(count)

# just remember that if u want to use an external variable in for loop you have to define it outsdie the for loop.