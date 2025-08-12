for tc in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    room = 0
    for i in range(2, n-2):
        max_high = 0
        for j in range(1, 3):
            if buildings[i-j] > max_high: max_high = buildings[i-j]
            if buildings[i+j] > max_high: max_high = buildings[i+j]
        if buildings[i] - max_high > 0:
            room += buildings[i] - max_high
    print(f'#{tc} {room}')