t = int(input())
for values in range(t):
  fill_water = 1
  not_fill = 2
  b1 ,b2, b3 = map(int,input().split())
  if b1 + b2 + b3 == 0:
    print("Water filling time")
  elif b1 + b2 + b3 == 3:
    print("Not now")
  elif b1 + b2 + b3 == 1:
    print("Water filling time")
  elif b1 + b2 + b3 == 2:
    print("Not now")

# check solution later