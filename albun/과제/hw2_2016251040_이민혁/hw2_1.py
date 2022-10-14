#분할정복

n = int(input())
map_input = [list(map(int, input().split()))
    for _ in range(n)]

w = 0
b = 0

def func(x, y, n):

    global w,b
    color = map_input[x][y]

    for i in range(x,x+n):
        for j in range(y, y+n):
            if color != map_input[i][j]:
                func(x, y, n//2)
                func(x, y+n//2, n//2)
                func(x+n//2, y, n//2)
                func(x+n//2, y+n//2, n//2)
                return 0

    if color == 0:
        w += 1
    else:
        b += 1

func(0, 0, n)
print(w)
print(b)
