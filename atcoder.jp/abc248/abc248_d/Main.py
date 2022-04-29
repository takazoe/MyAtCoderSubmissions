import sys
from bisect import bisect_left

#input
N = int(input())
lst_A = list(map(int, input().split()))
Q = int(input())

#calc
idx = [[] for _ in range(N+1)]
for i, a in enumerate(lst_A):
  idx[a].append(i)
  
for i in range(Q):
  L, R, X = map(int, input().split())
  print(bisect_left(idx[X], R) - bisect_left(idx[X], L-1))