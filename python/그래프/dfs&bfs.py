# DFS 반복문
def dfs(v):
    visited = [False] * (numV + 1)
    ST = []
    ST.append(v)

    # 방문처리
    print(v)
    visited[v] = True

    while ST:
        v = ST.pop()
        for w in G[v]:
            if not visited[w]:
                ST.append((w))
                print(w)
                visited[w] = True


numV = 7
inputV = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
G = [[] for _ in range(numV + 1)]
M = [[0] * (numV + 1) for _ in range(numV + 1)]

lst = list(map(int, inputV.split()))
for i in range(0, len(lst), 2):
    p1 = lst[i]
    p2 = lst[i + 1]
    G[p1].append(p2)    # 단방향
    G[p2].append(p1)    # 양방향: 위의 것과 같이 사용

    M[p1][p2] = 1   # 단방향
    M[p2][p1] = 1   # 양방향: 위의 것과 같이 사용

dfs(1)


# DFS 재귀
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# >>> 1 2 7 6 8 3 4 5




# BFS
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# >>> 1 2 3 8 7 4 5 6
