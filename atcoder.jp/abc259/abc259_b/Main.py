import math

# in
a,b,d = map(int,input().split())

# calc
d = math.radians(d)
x = a*math.cos(d) - b*math.sin(d)
y = a*math.sin(d) + b*math.cos(d)
  
# out
print(x,y)