from itertools import combinations

# in
A = []
h1, w1 = map(int, input().split())
for _ in range(h1):
    A.append(list(map(int, input().split())))
B = []
h2, w2 = map(int, input().split())
for _ in range(h2):
    B.append(list(map(int, input().split())))

# calc
# 0～h1を用いて要素数h2の組をつくる
for comb_h in combinations(range(h1), h2):
    # 0～w1を用いて要素数w2の組をつくる
    for comb_w in combinations(range(w1), w2):

        # Bの全ての要素がAと等しいかチェック
        check = True
        for i in range(h2):
            for j in range(w2):
                if B[i][j] != A[comb_h[i]][comb_w[j]]:
                    check = False
                    break
            if check is False:
                break
        if check:
            print("Yes")
            exit()

# out
print("No")