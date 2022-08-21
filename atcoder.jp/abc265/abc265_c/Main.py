# in
h,w = map(int, input().split())
M = []
for _ in range(h):
  M.append(input())

# calc
i,j = 0,0
S = set()
while True:
  s = str(i) + ":" + str(j)
  if s in S:
    print(-1)
    exit()
    
  g = M[i][j]
  if g == "U" and i != 0:
    i -= 1
  elif g == "D" and i != h-1:
    i += 1
  elif g == "L" and j != 0:
    j -= 1
  elif g == "R" and j != w-1:
    j += 1
  else:
    print(i+1,j+1)
    exit()
    
  S.add(s)