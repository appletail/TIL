inputV = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'


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

# print(G)
# print(M)
