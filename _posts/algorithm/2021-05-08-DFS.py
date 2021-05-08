N = int(input())

A = [list(map(int, list(input()))) for _ in range(N)]
ck = [0 for _ in range(N)]
dx, dy = [1, 0, -1, 0], dy[0, 1, 0, -1]
# 방향벡터: 동서남북??


def dfs(i, j):
    for way in range(4):
        ii, jj = i + dx[way], j + dy[way]
        if A[ii][jj] == 1:
            dfs(ii, jj)


for i in range(N):
    for j in range(N):
        if Ap[i][j] == 1:
            dfs(i, j)
