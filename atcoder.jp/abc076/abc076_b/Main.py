#in
N = int(input())
K = int(input())
 
#calc
c = 1
for _ in range(N):
  c = min(2*c, c+K)
  
#out
print(c)