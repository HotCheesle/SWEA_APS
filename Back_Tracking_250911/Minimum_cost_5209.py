def get_product(N, idx, cnt): 
    global min_cost
    if cnt == N: 
        min_cost = cal_cost(idx)
    for i in range(N): 
        if i not in idx: 
            nidx = idx+[i]
            if cal_cost(nidx) < min_cost: 
                get_product(N, nidx, cnt+1)

def cal_cost(idx): 
    if not idx: return 0
    tot_cost = 0
    for factory_idx in range(len(idx)): 
        tot_cost += products[idx[factory_idx]][factory_idx]
    return tot_cost

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    products = list(list(map(int, input().split())) for _ in range(N))
    min_cost = 9999
    get_product(N, [], 0)
    print(f'#{tc} {min_cost}')