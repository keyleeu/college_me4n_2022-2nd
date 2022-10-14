#bfs

from collections import deque


n, m = map(int, input().split())
graph= []
for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    answer = deque()
    answer.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while answer:
        a, b, w = answer.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if graph[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    answer.append([x, y, 0])
                elif graph[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    answer.append([x, y, w])
    return -1

print(bfs())