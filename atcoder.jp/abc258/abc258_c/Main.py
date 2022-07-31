# in
n,q = map(int,input().split())
S = input()
l = len(S)

# calc
c = 0
for _  in range(q):
  b,x = map(int,input().split())
  if b == 1:
    c += x
  else:
    print(S[(x-c-1)%l])