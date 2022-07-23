n = int(input())

S = {}
for i in range(n):
  s = input()
  if s in S:
    print(s + "(" + str(S[s]) + ")")
    S[s] += 1
  else:
    print(s)
    S[s] = 1