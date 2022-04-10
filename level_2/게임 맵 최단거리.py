from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dis = [[1] * (m) for _ in range(n)]
    ch = [[0] * (m) for _ in range(n)]
    Q = deque()
    Q.append((0, 0))
    ch[0][0] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and ch[nx][ny] == 0 and maps[nx][ny] == 1:
                ch[nx][ny] = 1
                dis[nx][ny] = dis[x][y] + 1
                Q.append((nx, ny))

    if dis[n - 1][m - 1] == 1:
        return -1
    else:
        return dis[n - 1][m - 1]