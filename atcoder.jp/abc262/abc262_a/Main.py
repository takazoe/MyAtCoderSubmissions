y = int(input())
if y%4 == 2:
  print(y)
else:
  print(y+(4-(y-2)%4))