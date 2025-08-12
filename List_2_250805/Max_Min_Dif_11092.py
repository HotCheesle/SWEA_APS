T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    min_idx, max_idx = 0, 0
    for i in range(N):
        if num_list[min_idx] > num_list[i]: min_idx = i
        if num_list[max_idx] <= num_list[i]: max_idx = i
    print(f'#{tc} {abs(min_idx - max_idx)}')
