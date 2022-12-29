# 반복문을 이용해 n개에서 r개를 고르는 조합
N = 5
R = 3
for i in range(N - R + 1):
    for j in range(i + 1, N - R + 2):
        for k in range(j + 1, N - R + 3):
            print(i, j, k)


# 재귀를 이용해 n개에서 r개를 고르는 조합
def nCr(n, r, s):
    if r == 0:
        print(comb)
    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            nCr(n, r - 1, i + 1)


A = [1, 2, 3, 4, 5]
n = len(A)
r = 3
comb = [0] * r
nCr(n, r, 0)
