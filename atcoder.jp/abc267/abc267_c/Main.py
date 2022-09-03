# in
n,m = map(int, input().split())
A = list(map(int, input().split()))

# calc
S = [0]
for i,a in enumerate(A):
  S.append(S[i] + a)

t = 0
for j in range(m):
  t += (j+1)*A[j]

ans = t
for i in range(n-m):
  t = t + S[i] - S[i+m] + A[i+m]*m
  ans = max(ans,t)

# out
print(ans)