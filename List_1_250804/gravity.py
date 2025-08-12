T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))
    max_drop = 0
    for i in range(N):
        if N-i < max_drop: break
        cnt = 0
        for j in range(i+1, N):
            if box_list[i] <= box_list[j]:
                cnt += 1
        if max_drop < (N-i-1-cnt):
            max_drop = N - i - 1 - cnt
    print(f'#{tc} {max_drop}')
