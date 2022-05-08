# in
N, A, B = map(int, input().split())

# calc
s1 = ""
s2 = ""
i = 0
for _ in range(N):
  for _ in range(B):
    if i%2 == 0:
      s1 += "."
      s2 += "#"
    else:
      s1 += "#"
      s2 += "."
  i += 1

# out
i = 0
for _ in range(N):
  for _ in range(A):
    if i%2 == 0:
      print(s1)
    else:
      print(s2)
  i += 1