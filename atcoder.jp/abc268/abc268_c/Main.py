n = int(input())
P = list(map(int, input().split()))

ANS = [0]*n
for i,p in enumerate(P):
  l = (p-i)%n
  ANS[(l-1)%n] +=1
  ANS[l] +=1
  ANS[(l+1)%n] +=1

print(max(ANS))