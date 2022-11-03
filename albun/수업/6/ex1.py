n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a.sort()
b.sort(reverse=True)
# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
# a의 원소가 b의 원소보다 작은 경우 교체
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))