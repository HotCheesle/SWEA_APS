T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_sum, max_sum = 0, 0
    for i in range(M):
        min_sum += num_list[i]
    max_sum = min_sum
    n_sum = min_sum
    for i in range(1, N-M+1):
        n_sum = n_sum + num_list[i+M-1] - num_list[i-1]
        if min_sum > n_sum: min_sum = n_sum
        if max_sum < n_sum: max_sum = n_sum
    print(f'#{tc} {max_sum - min_sum}')