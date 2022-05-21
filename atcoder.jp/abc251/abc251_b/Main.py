import itertools
 
# in
N, W = map(int, input().split())
A = list(map(int, input().split())) + [0, 0]
 
# calc
ans = 0
S = set() # 各ペアを判定
for x,y,z in itertools.combinations(A,3):
  s = x + y + z
  if s <= W:
    S.add(s)
  
# out
print(len(S))