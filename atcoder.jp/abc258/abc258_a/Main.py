k = int(input())
h = 21 + k//60
m = k%60
if m < 10:
  print(str(h)+":0"+str(m))
else:
  print(str(h)+":"+str(m))