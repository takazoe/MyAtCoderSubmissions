import numpy as np

# in
XY = []
for _ in range(4):
  x,y = map(int,input().split())
  XY.append(np.array([x,y]))
XY.append(XY[0])
XY.append(XY[1])

# calc
for i in range(4):
  v1 = np.array(XY[i]-XY[i+1])
  v2 = np.array(XY[i+2]-XY[i+1])
  cross = np.cross(v1,v2)
  if cross > 0:
    print("No")
    exit()  
  
# out 
print("Yes")