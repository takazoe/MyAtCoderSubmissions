n,x,y  = map(int,input().split())

R,B = [0]*10,[0]*10
R[n-1] += 1

for i in range(n-1,0,-1):
  R[i-1] += R[i]
  B[i] += R[i]*x
  R[i] = 0
  R[i-1] += B[i]
  B[i-1] += B[i]*y
  B[i] = 0
  
print(B[0])