# in
S = input()

# calc
ans = ""
if len(S) == 1:
  ans = S + S + S + S + S + S
elif len(S) == 2:
  ans = S + S + S
else:
  ans = S + S
    
# out
print(ans)