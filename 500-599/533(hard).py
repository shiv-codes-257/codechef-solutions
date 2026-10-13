n = int(input())
a = list(map(int,input().split()))
lucky = 0
unlucky = 0
for weapons in a:
  if weapons % 2 == 0:
    lucky += 1
  elif weapons % 2 != 0:
    unlucky += 1
if lucky > unlucky:
  print("READY FOR BATTLE")
else:
  print("NOT READY")

  # its fine to use other for loops even if not mentioned , you just need to get to the answer, and its ok to use other variables as well such as lucky , unlucky etc. unless they affect the result or parameters in some way.