# in
R, C = map(int, input().split())
A11, A12 = map(int, input().split())
A21, A22 = map(int, input().split())
A = [[A11, A12], [A21, A22]]

# out
print(A[R-1][C-1])