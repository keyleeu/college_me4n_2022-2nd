#bfs

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1] #순서대로 상 하 좌 우
dy = [1, -1, 0, 0]

# BFS
def bfs(x, y):
    answer = deque()
    answer.append((x,y))

    if graph[x][y] == 1:
        return False

    while answer:
        x, y = answer.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                answer.append((nx,ny))
                
    return True

cnt = 0

for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            cnt += 1

print(cnt)