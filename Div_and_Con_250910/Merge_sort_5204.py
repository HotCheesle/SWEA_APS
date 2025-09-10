def merge_sort(L, length): 
    global validate_cnt
    if length == 2:
        if L[0] > L[1]: 
            L[0], L[1] = L[1], L[0] 
            validate_cnt += 1
        return L
    elif length == 1: 
        return L
    llist = merge_sort(L[:length//2], length//2)
    rlist = merge_sort(L[length//2:], length//2+length%2)
    mlist = [0] * length
    if llist[-1] > rlist[-1]: 
        validate_cnt += 1
    lidx, ridx, midx = 0, 0, 0
    while lidx < len(llist) and ridx < len(rlist): 
        if llist[lidx] < rlist[ridx]: 
            mlist[midx] = llist[lidx]
            lidx += 1
            midx += 1
        else: 
            mlist[midx] = rlist[ridx]
            ridx += 1
            midx += 1
    if lidx != len(llist): 
        while lidx < len(llist): 
            mlist[midx] = llist[lidx]
            lidx += 1
            midx += 1
    else: 
        while ridx < len(rlist): 
            mlist[midx] = rlist[ridx]
            ridx += 1
            midx += 1
    return mlist

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    L = list(map(int, input().split()))
    validate_cnt = 0
    sorted_list = merge_sort(L, N)
    print(f'#{tc} {sorted_list[N//2]} {validate_cnt}')