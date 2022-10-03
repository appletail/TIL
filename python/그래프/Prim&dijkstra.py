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


# 가중치 계산 다익스트라
INF = int(1e9)

def dijk():
    U = []
    D = [INF] * (V+1)
    D[0] = 0
    P = [INF] * (V+1)

    while len(U) < V + 1:
        minV = INF
        # 가장 작은 노드를 찾음
        for i in range(V+1):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        # 해당 노드를 방문하는 작은 가중치로 갱신
        for i in range(V+1):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i] + D[curV]:
                D[i] = G[curV][i] + D[curV]
                P[i] = curV

    print(U, D, P)


V, E = map(int, input().split())

G = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

dijk()


# heapq를 이용하면 가장 작은 값을 찾는 연산인 부분을 O(n)에서 O(log n) 으로 바꿀 수 있음
import heapq

INF = int(1e9)


def dijk():
    U = []
    D = [INF] * (V+1)
    D[0] = 0
    P = [INF] * (V+1)

    q = []
    heapq.heappush(q, (0, 0))

    while len(U) < V + 1:
        # 가장 작은 노드를 찾음
        weight, curV = heapq.heappop(q)
        if curV in U: continue

        U.append(curV)

        # 해당 노드를 방문하는 작은 가중치로 갱신
        for i in range(V+1):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i] + D[curV]:
                D[i] = G[curV][i] + D[curV]
                P[i] = curV
                heapq.heappush(q, (D[i], i))

    print(U, D, P)


V, E = map(int, input().split())

G = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

dijk()

