def backtracking(n, sum): 
    global min_sum
    if n == N: 
        if sum < min_sum: 
            min_sum = sum
        return None
    elif sum >= min_sum: 
        return None
    for i in range(n, N): 
        index[n], index[i] = index[i], index[n]
        backtracking(n+1, sum+arr[n][index[n]])
        index[n], index[i] = index[i], index[n]
    


T = int(input())
for tc in range(1, T+1): 
    min_sum = 10000
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    index = [i for i in range(N)]
    backtracking(0, 0)
    print(f'#{tc} {min_sum}')