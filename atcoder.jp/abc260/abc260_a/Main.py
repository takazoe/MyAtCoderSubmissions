S = input()

t = ""
c = 1
for s in S:
  c = 0
  for s2 in S:
    if s == s2:
      c += 1
  if c == 1:
    print(s)
    exit()

print(-1)