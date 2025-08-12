for tc in range(1, 11):
    dump_cnt = int(input())
    land = list(map(int, input().split()))

    counts = [0 for _ in range(101)]
    total = 0 # 총 상자의 개수
    max_dump = 0

    for h in land:
        counts[h] += 1
        total += h

    middle = total // 100

    for i in range(1, middle+1): # 누적 카운트 세기 이때 숫자는 해당 레벨의
        counts[i] += counts[i-1] # 공간을 매우기 위해 필요한 덤프의 양이 된다.
    for i in range(99, middle, -1):
        counts[i] += counts[i+1]

    for i in range(middle + 1):
        max_dump += counts[i]
    if dump_cnt >= max_dump: # 필요 덤프횟수보다 더 많은 덤프횟수가 주어졌을 때
        if total % 100 == 0: # 상자가 100으로 나누어 떨어지면 0
            print(f'#{tc} 0')
            continue
        else:  # 아니면 1
            print(f'#{tc} 1')
            continue

    low, high = 0, 100
    low_used, high_used = 0, 0

    while low_used <= dump_cnt:
        low_used += counts[low]
        low += 1
    while high_used <= dump_cnt:
        high_used += counts[high]
        high -= 1

    print(f'#{tc} {high - low + 2}')
