# in
H,W = map(int, input().split())

# calc
X,Y = [],[]
for i in range(H):
  s = input()
  for j,t in enumerate(s):
    if t == "o":
      X.append(i)
      Y.append(j)
ans = abs(X[0]-X[1]) + abs(Y[0]-Y[1]) 
    
# out
print(ans)