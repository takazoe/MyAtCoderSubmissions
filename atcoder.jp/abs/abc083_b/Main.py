#input
n,a,b = map(int, input().split())
#calc
total_i = 0
for i in range(1,n+1):
  #sum
  lst_j = list(map(int, str(i)))
  total_j = sum(lst_j)
  if a <= total_j <= b:
    total_i += i
  
#out
print(total_i)