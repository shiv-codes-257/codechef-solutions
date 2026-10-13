t = int(input())
for values in range(t):
  a,b,c = map(int,input().split())
  if (a+b)/2 < c:
    print("YES")
  else:
    print("NO")