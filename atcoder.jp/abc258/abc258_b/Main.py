# in
n = int(input())
A = []
for _ in range(n):
  row = input()
  A.append(row + row + row)
A += A + A

# calc
ans = 0
for i in range(n, 2*n):
  for j in range(n, 2*n):
    for di in range(-1,2):
      for dj in range(-1,2):
        if di == 0 and dj == 0:
          continue
        s = ""
        for k in range(n):
          s += A[i+di*k][j+dj*k]
        ans = max(int(s),ans)

# out
print(ans)