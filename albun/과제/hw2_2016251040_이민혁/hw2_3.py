#이분탐색

n,m = map(int, input().split())

up = []
down = []

for i in range(n):
    
    if i % 2 == 0: # 짝수인지 체크
        down.append(int(input()))
    else:
        up.append(int(input()))

up.sort()
down.sort()

min = n
range_input = 0

def bst(arr, x, left, right):

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid +1
        else:
            right = mid -1

    return left

for i in range(1, m + 1):

    bottom = len(down) - bst(down, i - 0.5, 0, len(down) - 1)
    top = len(up) - bst(up, m - i + 0.5, 0, len(up) - 1)

    if min == bottom + top:
        range_input += 1
    elif min > bottom + top:
        range_input = 1
        min = bottom + top
    
print(min, range_input)