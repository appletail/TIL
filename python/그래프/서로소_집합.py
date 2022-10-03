# 집합 만들기
# make-set(a) ~ (f)
#         a b c d e f
#     i   0 1 2 3 4 5
# => tree 0 1 2 3 4 5

# 빈리스트를 만들고 하나씩 함수로 만들기
def make_set(x):
    p[x] = x

# 한 번에 여러개의 집합 만들기
# p = [i for i in range(N + 1)]


# 집합의 대표원소 찾기
# 재귀보다는 반복문으로 하는 것을 추천
# 반복문
def find_setW(v):
    while p[v] != v:
        v = p[v]
    return v

# 재귀
def find_setR(v):
    if v == p[v]:
        return v
    else:
        return find_setR(p[v])

# 유니온
# union(c, d), union(e, f)
#         a b c d e f
#     i   0 1 2 3 4 5
# => tree 0 1 2 2 4 4

# union(d, f)
# 1. d의 대표원소를 찾는다
# 2. f의 대표원소를 찾는다
# 3. f의 대표원소를 d의 대표원소로 교체
#         a b c d e f
#     i   0 1 2 3 4 5
# => tree 0 1 2 2 2 4

def union(a, b):
    # r1 = find_setW(a)
    # r2 = find_setR(b)
    # p[r2] = r1
    p[find_setR(b)] = find_setW(a)

# 트리의 수(집합의 수)
# 자기 자신이 대표인 것의 수 == 트리의 수
# cnt = 0
# for i in range(1, N + 1):
#     if p[i] == i:
#         cnt += 1


def find_setW(v):
    while p[v] != v:
        v = p[v]
    return v


def union(a, b):
    p[find_setR(b)] = find_setW(a)


N = 6
p = [i for i in range(N + 1)]

cnt = 0
for i in range(1, N + 1):
    if p[i] == i:
        cnt += 1


# 1. Rank를 이용한  Union
#     - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크 Rank라는 이름으로 저장
# p[x] : 노드 x의 부모 저장
p = [i for i in range(N)]
# rank[x] : 루트 노드가 x인 트리의 랭크값 저장
rank = [0] * N


def make_set(x):
    p[x] = x
    rank[x] = 0


def union_Rank(x, y):
    Link(find_set(x), find_set(y))


def Link(x, y):
    if rank[x] > rank[y]:  # rank는 트리의 높이
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

#     - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙임
# 2. Path compression
#     - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꿔줌
def find_set(x):
    if x != p[x]:  # x가 루트가 아닌 경우
        p[x] = find_set(p[x])
    return p[x]