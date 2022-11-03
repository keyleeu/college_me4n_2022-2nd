# dijistra 알고리즘

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [INF] * (n+1)
start = 1
q = []
dist[1] = 0

def dijistra():
    heapq.heappush(q,(0,start))
    while q:
        distance,x = heapq.heappop(q)
        if distance > dist[x]:
            continue
        for i in graph[x]:
            cost = distance + 1
            if cost < dist[i]:
                dist[i] = cost
                heapq.heappush(q,(cost,i))

    b = max(dist[1:])
    a = dist.index(b)
    c = dist.count(b)

    print(a,b,c)

dijistra()

