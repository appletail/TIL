# 반복문을 이용한 순열
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)


# 재귀를 통한 순열1
def f(i, k):
    if i == k:      # 인덱스 i == 원소의 개수
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
f(0, 3)


# 재귀를 통한 순열2
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 사용됨으로 표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i + 1, k)     # p[i + 1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제


N = 3
a = [i for i in range(1, N + 1)]
used = [0] * N
p = [0] * N
f(0, N)


# 10개 중 3개만 고르고 싶을 때
def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 사용됨으로 표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i + 1, k, r)  # p[i + 1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제


N = 10
R = 3
a = [i for i in range(1, N + 1)]
used = [0] * N
p = [0] * R
f(0, N, R)
