t = int(input())
for values in range(t):
  n,x = map(int,input().split())
  if n <= 6:
    print(x)
  elif n > 6 and n % 6 == 0:
    print(int((n/6)*x))
  elif n > 6 and n % 6 != 0:
    print(int(((n//6)+1)*x))