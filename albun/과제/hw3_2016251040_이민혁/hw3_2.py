#dfs

n = int(input())
number = list(map(int, input().split()))
operation = list(map(int, input().split()))
max_ans = -int(1e9)
min_ans = int(1e9)

answer = number[0]

def dfs(alpa):
    global answer
    global max_ans
    global min_ans

    if alpa == n:
        if answer > max_ans:
            max_ans = answer
        if answer < min_ans:
            min_ans = answer
        return
    
    for i in range(4):
        tmp = answer
        if operation[i] > 0:
            if i == 0:
                answer += number[alpa]
            elif i == 1:
                answer -= number[alpa]
            elif i == 2:
                answer *= number[alpa]
            else:
                if answer >= 0:
                    answer //= number[alpa]
                else:
                    answer = (-answer // number[alpa]) * -1
        
            operation[i] -= 1
            dfs(alpa+1)
            answer = tmp
            operation[i] += 1

dfs(1)
print(max_ans)
print(min_ans)

        