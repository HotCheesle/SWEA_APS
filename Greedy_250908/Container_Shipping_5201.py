T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    # 트럭 내부에 남는 공간이 최소가 되면 가장 많이 실은 것임 
    # 아 tq 트럭당 하나의 컨테이너였고...
    tot_weight = 0
    if container[-1] > truck[0]: 
        print(f'#{tc} {tot_weight}')
        continue
    for cargo in container: 
        for idx in range(M): 
            if truck[idx] >= cargo: 
                tot_weight += cargo
                truck[idx] = 0
                break
    print(f'#{tc} {tot_weight}')