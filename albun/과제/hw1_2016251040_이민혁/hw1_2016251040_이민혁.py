def dfs(f):
    global cnt
    x, y, z = f

    #끝에 도달한경우
    if (x, y) == (n-1, n-1):
        cnt += 1
        return

    #대각선 이동
    if x+1 < n and y+1 < n:
        if graph[x+1][y+1] == 0 and graph[x][y+1] == 0 and graph[x+1][y] == 0:
            dfs((x+1, y+1, 2))

    #가로 이동
    if z == 0 or z == 2:
        if y+1 < n:
            if graph[x][y+1] == 0:
                dfs((x, y+1, 0))

    #세로 이동
    if z == 1 or z == 2:
        if x+1 < n:
            if graph[x+1][y] == 0:
                dfs((x+1, y, 1))

cnt = 0 #초기화
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

dfs((0, 1, 0)) #처음 차지하고 있는 파이프의 위치
print(cnt)

#아직 관련 코딩 능력이 부족해 알고리즘과 코드를 카피 해왔습니다. 
#여러 알고리즘을 비교해 보며 이해는 했지만 언제 어떤걸 사용해야하는지에는 미숙한것 같습니다.
#다음 과제 때에는 직접 짤수 있도록 노력하겠습니다. 죄송합니다..