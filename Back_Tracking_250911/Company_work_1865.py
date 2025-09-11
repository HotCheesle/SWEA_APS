def get_work(N, idx, cnt): 
    global max_prop
    if cnt == N: 
        max_prop = cal_prop(idx)
    for i in range(N): 
        if i not in idx and workers[cnt][i] != 0: 
            nidx = idx+[i]
            if cal_prop(nidx) >= max_prop: 
                get_work(N, nidx, cnt+1)

def cal_prop(idx): 
    if not idx: return 100.0
    tot_prop = 100.0
    for work_idx in range(len(idx)): 
        tot_prop *= workers[work_idx][idx[work_idx]]
    return tot_prop

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    workers = []
    for _ in range(N): 
        success = tuple(map(lambda s: int(s)/100, input().split()))
        workers.append(success)
    max_prop = 0.0
    get_work(N, [], 0)
    print(f'#{tc} {max_prop:.6f}')