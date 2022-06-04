# in
N = int(input())

# calc
print(1)
if N==1:
  exit()

A_old = [1]
for i in range(1,N):
  A = [1]
  for j in range(1,i):
    A.append(A_old[j-1] + A_old[j])
  A.append(1)
  print(*A)
  A_old = A