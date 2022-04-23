#input
n = input()
lst_i = list(map(int, input().split()))

lst_i = sorted(lst_i)[::-1]
total = 0
j=1
for i in lst_i:
  total += i*j
  j *= -1
  
#out
print(total)