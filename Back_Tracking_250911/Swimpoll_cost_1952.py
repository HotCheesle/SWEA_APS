def get_poss_tm(st, poss): 
    if st > 9: 
        triple_plan.append(poss)
        return
    for s in range(st, 10): 
        get_poss_tm(s+3, poss+[s])

triple_plan = []
get_poss_tm(0, [])

T = int(input())
for tc in range(1, T+1): 
    D, M, TM, Y = map(int, input().split())
    monthly_plan = list(map(int, input().split()))
    cost_plan = list(map(lambda i: i*D ,monthly_plan))
    for m in range(12): 
        if cost_plan[m] > M: 
            cost_plan[m] = M
    max_gain = 0
    for triple in triple_plan: 
        tot_gain = 0
        for tm in triple: 
            gain = sum(cost_plan[tm:tm+3]) - TM
            if gain <= 0: 
                break
            else: 
                tot_gain += gain
        if max_gain < tot_gain: 
            max_gain = tot_gain
    tot_cost = sum(cost_plan) - max_gain
    if tot_cost > Y: 
        tot_cost = Y
    print(f'#{tc} {tot_cost}')