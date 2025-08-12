def binary_search_cnt(n, key): 
    cnt = 0
    left = 1
    right = n
    while left <= right: 
        cnt += 1
        mid = (left + right) // 2
        if mid == key: 
            return cnt
        elif mid < key: 
            left = mid
        else: 
            right = mid
    return -1

T = int(input())
for tc in range(1, T+1): 
    N, A, B = map(int, input().split())

    A_cnt = binary_search_cnt(N, A)
    B_cnt = binary_search_cnt(N, B)
    if A_cnt == B_cnt: 
        print(f'#{tc} 0')
    elif A_cnt < B_cnt: 
        print(f'#{tc} A')
    else: 
        print(f'#{tc} B')