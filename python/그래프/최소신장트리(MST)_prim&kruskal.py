# 최소 신장 트리 (Minimum Spanning Tree)
# 무방향 가중치 그래프에서 신장 트리를 구설하는 간선들의 가중치의 합이 최소인 신장 트리
'''
입력값
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


# key값을 계속 바꾸고 MST에 넣어 확정시키는 방식
def prim1(r, V):  # r: 시작정점 V: 마지막 정점 번호
    MST = [0] * (V + 1)  # MST 포함여부 판단을 위한 리스트
    key = [10000] * (V + 1)  # 가중치의 최대값 이상으로 초기화. key[v]는 MST에 속해있는 정점과 연결된 정점들의 가중치
    key[r] = 0  # 시작정점의 key
    for _ in range(V):  # V + 1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[u] == 0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        # 가중치들 중 가장 작은 노드 추가
        for i in range(V + 1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1  # 정점 u를 MST에 추가
        # MST에 포함되지 않고, u에 인접인 v라면
        # 최소 가중치로 갱신
        for v in range(V + 1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])  # 기존의 가중치와 새로 연결된 노드와의 가중치와 비교하여 더 작은 가중치로 갱신

    return sum(key)  # MST 가중치의 합


# MST와 연결된 모든 노드를 돌면서 가장 작은 가중치를 더하는 방식
def prim2(r, V):
    MST = [0] * (V + 1)  # MST 포함여부
    MST[r] = 1  # 시작정점 표시
    s = 0  # MST 간선의 가중치 합
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V + 1):
            if MST[i] == 1:  # MST에 포함된 정점이면
                for j in range(V + 1):  # 그 정점과 인접한 모든 정점 중 최소값
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1

    return s


V, E = map(int, input().split())    # V: 마지막 정점, 0 ~ V번 정점
adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 인접 행렬
adjL = [[] for _ in range(V + 1)]  # 인접 리스트
for _ in range(E):
    u, v, w = map(int, input().split())
    # 인접 행렬에 저장 방법
    adjM[u][v] = w  # u에서 v사이의 가중치가 w다
    adjM[v][u] = w  # v에서 u사이의 가중치가 w다
    # 인접 리스트 저장 방법
    adjL[u].append((v, w))  # u에서 v사이의 가중치가 w다
    adjL[v].append((u, w))  # v에서 u사이의 가중치가 w다

print(prim1(0, V))
print(prim2(0, V))


# KRUSKAL 알고리즘
# 1) 가중치 순으로 오름차순 정렬
# 2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
#   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
# 3) n - 1개의 간선이 선택될 때까지 2)를 반복
# 서로소 집합을 사용
# 대표 원소가 같으면 사이클로 판단하고 넘어감
# 대표 원소가 다르면 연결시킴
def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x: x[2])
rep = [i for i in range(V + 1)]  # 대표원소 배열

N = V + 1  # 실제 정점 수
cnt = 0  # 선택한 edge의 수
total = 0  # MST 가중치의 합
for u, v, w in edge:
    if find_set(u) != find_set(v):  # 대표가 같으면 사이클이라는 뜻이라 연결안함
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:  # 간선 수
            break

print(total)