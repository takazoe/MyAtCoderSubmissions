# in
n, x = map(int, input().split())

# calc
s = ""
I = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in I:
  for _ in range(n):
    s+=i
    
# out
print(s[x-1])