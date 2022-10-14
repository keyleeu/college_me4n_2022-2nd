#dfs

def dfs(x, y, move, total):

    global answer

    if total + max_value*(4-move) <= answer:
        return

    if move == 4:
        answer = max(answer, total)
        return
    
    for plus_x, plus_y in plus_move:
        new_x = x + plus_x
        new_y = y + plus_y

        if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]:
            if move == 2:
                visited[new_x][new_y] = True
                dfs(x, y, move+1, total+map_input[new_x][new_y])
                visited[new_x][new_y] = False
            visited[new_x][new_y] = True
            dfs(new_x, new_y, move+1, total+map_input[new_x][new_y])
            visited[new_x][new_y] = False


if __name__ == "__main__":
    n,m = map(int, input().split())
    map_input = [list(map(int, input().split()))
        for _ in range(n)]
    max_value = max(map(max, map_input))
    plus_move = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False] * m for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, 1, map_input[i][j])
            visited[i][j] = False
    print(answer)