#input
n, Y = map(int, input().split())

#culc
x,y,z = -1,-1,-1
for a in range(n + 1):
  for b in range(n + 1):
    c = n - a - b
    total = 10000*a + 5000*b + 1000*c
    if total > Y or c < 0:
      break
    if total == Y:
      print(a,b,c)
      x,y,z = a,b,c
      exit()     
      
#out
print(x,y,z)