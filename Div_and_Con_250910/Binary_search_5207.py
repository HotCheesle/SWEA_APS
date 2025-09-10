def binary_search(st, ed, find, direc): 
    global cnt
    m = (st+ed)//2
    if A[m] == find: 
        cnt += 1
        return
    elif st > ed: 
        return
    elif A[m] < find and direc != 1: 
        binary_search(m+1, ed, find, 1)
    elif A[m] > find and direc != -1: 
        binary_search(st, m-1, find, -1)
    else: 
        return

T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for find in B: 
        binary_search(0, N-1, find, 0)
    print(f'#{tc} {cnt}')