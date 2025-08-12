T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()
    counts = [0 for _ in range(10)]
    for card in cards:
        counts[int(card)] += 1
    most = 0
    for i in range(10):
        if counts[most] <= counts[i]:
            most = i
    print(f'#{tc} {most} {counts[most]}')