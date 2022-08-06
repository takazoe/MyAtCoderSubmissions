import itertools

# in
n,m = map(int,input().split())

# calc
ANS = list(itertools.combinations(range(1,m+1), n))

# out
for ans in ANS:
  print(*ans)