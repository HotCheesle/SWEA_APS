T = int(input())
for tc in range(1, T+1): 
    min_heap = [None]
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(N): 
        min_heap.append(num_list[i])
        leaf = i+1
        while leaf != 1 and min_heap[leaf] < min_heap[leaf//2]: 
            min_heap[leaf], min_heap[leaf//2] = min_heap[leaf//2], min_heap[leaf]
            leaf //= 2
    tot = 0
    leaf = (len(min_heap)-1) // 2
    while leaf != 0: 
        tot += min_heap[leaf]
        leaf //= 2
    print(f'#{tc} {tot}')