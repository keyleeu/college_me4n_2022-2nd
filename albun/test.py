#1-N 번ㅈ까지의 건물

n,m = map(int, input().split())
edges =[]
result = 0

for i in range(m):
    a,b = map(int, input().split())
    edges.append((a,b))
x,k = map(int, input().split())

def bfs(x,y):
    q = deque()
    q.append((x,y))

    d