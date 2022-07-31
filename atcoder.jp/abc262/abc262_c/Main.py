n = int(input())
A = list(map(int,input().split()))

ans,c = 0,0
for i in range(n):
  if A[i] == i+1:
    c += 1
  elif A[A[i]-1] == i+1:
    if A[i]-1 > i:
      ans += 1
if c > 1:
  ans += c*(c-1)/2
print(int(ans))