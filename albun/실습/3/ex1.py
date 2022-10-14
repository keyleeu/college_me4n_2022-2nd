#1.정렬 (nlogn)
#2.탐색 (mlogn)
#3.이분탐색으로 접근해야한다 / 시간복잡도를 이용하여


def bst(array, key, start, end):
    array = array.sort()
    start = 0
    end = len(array) - 1


n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
