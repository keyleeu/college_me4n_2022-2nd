def bst(x, array):

    array.sort()
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + end // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            start = mid + 1
        elif array[mid] > x:
            end = mid - 1

    return None    

array = [1,2,3,4,6,8,10,15,18,20,30,40,100,200,500]
x=30