#kruskal

n,m = map(int, input().split())
edges = []
result = 0
for i in range(m):
    x,y,cost = map(int, input().split())
    edges.append((cost,x,y))
    result += cost
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result -= cost

print(result)