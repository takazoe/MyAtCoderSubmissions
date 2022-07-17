n,x,y,z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AB = [x + y for (x, y) in zip(A, B)]

zip_lists = zip(A, range(0,-n,-1))
zip_sort = sorted(zip_lists, reverse=True)
A, idx_A = zip(*zip_sort)

zip_lists = zip(B, range(0,-n,-1))
zip_sort = sorted(zip_lists, reverse=True)
B, idx_B = zip(*zip_sort)

zip_lists = zip(AB, range(0,-n,-1))
zip_sort = sorted(zip_lists, reverse=True)
AB, idx_AB = zip(*zip_sort)

idx_G = set(idx_A[:x])

for b,idx_b in zip(B, idx_B):
  if idx_b in idx_G:
    continue
  elif len(idx_G) < x+y:
    idx_G.add(idx_b)

for ab,idx_ab in zip(AB, idx_AB):
  if idx_ab in idx_G:
    continue
  elif len(idx_G) < x+y+z:
    idx_G.add(idx_ab)

for ans in sorted(list(idx_G), reverse=True):
  print(ans*-1 + 1)
