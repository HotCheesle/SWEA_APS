T = int(input())

for tc in range(1, T+1):
    course = [0 for _ in range(5000)]
    start, end = [], []
    N = int(input())
    for i in range(N):
        st, ed = map(int, input().split())
        start.append(st)
        end.append(ed)
    point_cnt = int(input())
    bus_stop = []
    for i in range(point_cnt):
        bus_stop.append(int(input()))
    for i in range(N):
        for j in range(start[i]-1, end[i]):
            course[j] += 1
    print(f'#{tc}', end=' ')
    for i in range(point_cnt):
        print(course[bus_stop[i]-1], end=' ')
    print()