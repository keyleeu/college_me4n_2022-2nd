n, m = map(int, input().split())
home_input = map(int, input().split())

home_input = []

left = 0
right = n

while left >= right:
    if left == right:
        mid = 0
    elif left <=right:
        mid = (left + right) // 2
    

#def bst(x_arr, x, ):
#    x_arr = home_input
    

print(mid)

#print(dis)

#첫째줄에 가장 인접한 두 공유기 사이의 최대거리
#공유기 c개
#한집에 하나
#가장 인접한 두 공유기 사이 거리최대

#집의개수 n
#공유기의 개수 c
#집의 좌표 home_input / arr값
#공유기 사이의 거리 dis

#중간값을 찾는 과정 - 중간값을 찾은뒤 / 그 다음 중간값
#마지막 줄에서는 dis가 가장 커질수 있는 경우의 x 값을 찾아야함
#bst / ?