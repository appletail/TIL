'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


# prim 알고리즘
# 교재 73 페이지
def prim():
    U = []
    D = [10000] * (N + 1)  # 밸류
    P = [10000] * (N + 1)  # 스타트
    D[0] = 0

    while len(U) < (N + 1):
        # curV = U에 D 중 가장 작은 값을 가진 정점을 선택
        minV = 10000
        for i in range(N + 1):
            if i in U:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 정점들의 D값을 최선으로 바꿔준다.
        for i in range(N + 1):
            if i in U:
                continue
            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
                P[i] = curV
    print(U, D, P)


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w
    G[n2][n1] = w

prim()


'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''


# dijkstra 알고리즘
def dijk():
    U = []
    D = [10000] * (N + 1)
    D[0] = 0
    while len(U) < (N + 1):
        # D가 최선인 curV를 선택
        minV = 10000
        for i in range(N + 1):
            if i in U:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 D의 값을 수정
        for i in range(N + 1):
            if i in U:
                continue
            if G[curV][i] and D[i] > D[curV] + G[curV][i]:
                D[i] = D[curV] + G[curV][i]
    print(U, D)


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

dijk()