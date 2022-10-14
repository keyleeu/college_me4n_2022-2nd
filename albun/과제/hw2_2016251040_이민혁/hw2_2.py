#이분탐색

n, m = map(int, input().split())
list_input = list(map(int, input().split()))

left = 1
right = sum(list_input)

while left <= right:

    mid = (left + right) // 2
    cnt = 0 # 비어있는 값

    for a in list_input: # a = 떡볶이
        if a > mid: 
            cnt += a - mid
    
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)