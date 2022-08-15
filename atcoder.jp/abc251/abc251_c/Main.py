# in
n = int(input())

# calc
mx_score = 0
mx_i = 0
S = set()
for i in range(n):
  s,t = input().split()
  if s in S:
    continue
  S.add(s)
  if int(t) > mx_score:
    mx_score = int(t)
    mx_i = i+1
    
# out
print(mx_i)