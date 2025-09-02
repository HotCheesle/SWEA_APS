"""
TC는 총 15개, 제한시간은 2초이므로 총 약 6000만번 가능하고 각 TC마다 400만번 연산 가능하다.
N <= 1000 이고, 전봇대 높이 A, B <= 10000 이므로 10000배열에 각 전선마다 길이만큼 더한다고 하면
5000*1000 = 500만번 이므로 다른 방법이 필요해 보인다. 문제 잘못읽음 총 포인트의 개수였다
시작점과 끝점을 기록한 뒤 스택에 넣어서 한번의 순회로 계산이 가능하다.
스택으로 하면 예외가 많이 발생함 따라서 그냥 1000개의 전선의 시작점과 끝점을 넣고 해당 전선에 대해서 겹치는
포인트를 모두 센뒤 2로 나눠주면 된다. 시작점이 자신보다 낮으면 끝점이 자신보다 커야하고 시작점이 자신보다 높으면
끝점이 자신보다 낮아야 포인트가 생성된다.
"""

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    wire_st, wire_ed = [0 for _ in range(1000)], [0 for _ in range(1000)]
    for i in range(N): 
        st, ed = map(int, input().split())
        wire_st[i] = st
        wire_ed[i] = ed
    tot_point = 0
    for i in range(N): 
        start, end = wire_st[i], wire_ed[i]
        for other in range(N): 
            if i == other: continue
            if wire_st[other] < start:   # 시작이 자신보다 낮으면
                if wire_ed[other] > end: # 끝이 자신보다 높아야 겹친다
                    tot_point += 1
            else:                        # 시작이 자신보다 높으면
                if wire_ed[other] < end: # 끝이 자신보다 낮아야 겹친다
                    tot_point += 1
    print(f'#{tc} {tot_point//2}')