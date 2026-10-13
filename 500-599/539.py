t = int(input())
for values in range(t):
  x,y = map(int,input().split())
  if x*y == 100:
    print("1")
  elif x*y < 100:
    print("0")
  elif x*y > 100:
    print((x*y)//100)