# in
n = int(input())
A = list(map(int, input().split()))

#calc
M = []
p = 0
for a in A:
  M.append(0)
  M = [m+a for m in M]
  P = [m for m in M if m > 3]

# out
print(len(P))