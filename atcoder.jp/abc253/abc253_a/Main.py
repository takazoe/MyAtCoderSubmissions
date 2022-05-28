# in
a,b,c = map(int,input().split())

# out
if (a<=b and b<=c) or (a>=b and b>=c):
  print("Yes")
else:
  print("No")