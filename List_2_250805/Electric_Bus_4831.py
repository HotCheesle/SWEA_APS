T = int(input())

for tc in range(1, T+1):
    battery, length, charger = map(int, input().split())
    course = [0 for _ in range(length)]
    charge_point = list(map(int, input().split()))
    impossible = False

    for i in range(charger):
        course[charge_point[i]] = 1
        if i != 0:
            if charge_point[i] - charge_point[i-1] > battery:
                impossible = True
                break
    if impossible:
        print(f'#{tc} 0')
        continue

    bus, charge_cnt = 0, 0
    while bus < length:
        far = 0
        for i in range(1, battery+1):
            if bus + i >= length:
                bus = length
                break
            if course[bus + i] == 1:
                far = i
        bus += far
        charge_cnt += 1
    print(f'#{tc} {charge_cnt-1}')