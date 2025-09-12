from collections import defaultdict as ddict

def numbers_idx(cnt, end, index, tot): 
    if cnt == end: 
        poss_score.add(tot)
        return
    for idx in range(cnt, end): 
        for times in range(1, ndict[number[idx]]+1): 
            numbers_idx(cnt+1, end, index+[idx], tot+(number[idx]*times))
        numbers_idx(cnt+1, end, index+[idx], tot)

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    num_list = list(map(int, input().split()))
    ndict = ddict(int)
    poss_score = set()
    for num in num_list: 
        ndict[num] += 1
    number = list(ndict.keys())
    numbers_idx(0, len(number), [], 0)
    print(f'#{tc} {len(poss_score)}')