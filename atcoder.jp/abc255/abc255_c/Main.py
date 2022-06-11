# in
x,a,d,n = map(int, input().split())

# calc
e = a + d * (n-1)

if d == 0:
  print(abs(a - x))
  
elif (0 < d and x <= a) or (d < 0 and a <= x):
  print(abs(a - x))
  
elif (0 < d and e <= x) or (d < 0 and x <= e):
  print(abs(e - x))
  
else:
  dis_a = (x-a) % d
  dis_e = d - dis_a
  print(min(abs(dis_a), abs(dis_e)))