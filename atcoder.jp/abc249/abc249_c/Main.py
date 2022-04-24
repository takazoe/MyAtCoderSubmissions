import itertools

#input
n,k = map(int, input().split())

s = []
for i in range(n):
  s.append(input())
  
#calc
s_pairs = []
for i in range(1, n+1):
    s_pairs += itertools.combinations(s, i)

count_max = 0
num = 0
for pairs in s_pairs:
  s_all = "".join(pairs)
  s_uniq = "".join((list(set(s_all))))
  #count
  count = 0
  for j in s_uniq:
    if s_all.count(j) == k:
      count += 1
  #if max
  if count_max < count:
    count_max = count

#out
print(count_max)