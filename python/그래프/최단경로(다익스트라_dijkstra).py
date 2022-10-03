# 다익스트라 (음의 가중치가 없는 경우에 사용 가능)
# 알고리즘 루틴
# 1. 현재 노드와 인접한 노드 간의 거리를 표시할 배열 생성 (D)
# 2. 방문한 노드를 표시할 배열 생성 (U)
# 3. U에 시작 정점 s 추가
# 4. s와 인접한 모든 정점과의 거리를 D에 표시
# 5. U가 모두 채워질때까지 아래 순서를 반복
# 6. D 중에서 U에 포함 안된 정점들 중 거리가 가장 짧은 정점을 선택(w)하여 U에 추가
# 7. 기존의 거리와 여태까지 연결된 거리와 비교하여 노드의 거리를 비교하여 더 작은 값을 D에 추가
#   ex) a(s) → c: 4 / a(s) → b(w) → c : 3 인 경우 D배열 중 c를 나타내는 값을 3으로 갱신
# 8. 반복이 끝나면 D배열에서 목표 정점의 값을 리턴
#    ※ D에는 시작 정점(s)에서 각 정점으로 가는 최단 경로만 남아있음

def dijk():
    U = []
    D = [10000] * (N + 1)
    D[0] = 0
    while len(U) < (N + 1):
        # D가 최선인 curV를 선택
        minV = 10000
        for i in range(N + 1):
            if i not in U and minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)
        # curV하고 연결된 D의 값을 수정
        for i in range(N + 1):
            if i not in U and G[curV][i]:
                D[i] = min(D[i], D[curV] + G[curV][i])
    print(U, D)


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

dijk()


# 경로를 알아내는 방법
def dijk():
    U = []
    D = [1e9] * (V+1)
    D[0] = 0
    P = [1e9] * (V+1)

    while len(U) < V + 1:
        minV = 1e9
        # 가장 작은 노드를 찾음
        for i in range(V+1):
            if i not in U and minV > D[i]:
                minV = D[i]
                curV = i

        U.append(curV)

        # 해당 노드를 방문하는 작은 가중치로 갱신
        for i in range(V+1):
            if i not in U and G[curV][i]:
                D[i] = min(D[i], D[curV] + G[curV][i])
                P[i] = curV

    print(U, D, P)


V, E = map(int, input().split())
G = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

dijk()
# P: [1000000000.0, 0, 1, 1, 2, 3]
# 5번으로 가기 위해서는 역순으로 보면 됨
# 5 → 3 → 1 → 0
# 0 → 1 → 3 → 5 순으로 움직임
