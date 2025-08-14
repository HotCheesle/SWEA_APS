T = int(input())
for tc in range(1, T+1): 
    string = list(input().split())
    N = int(string[0])
    b_move, b_btn, o_move, tot_time, o_btn = 0, 1, 0, 0, 1
    # move: 움직일 수 있는 거리, tot_time: 총 걸린 시간, btn: 현재 서있는 위치의 버튼번호
    for btn in range(1, N+1): 
        if string[btn*2-1] == 'B': 
            time = abs(b_btn - int(string[btn*2])) # 이전 위치에서 버튼을 누르러 가는데 걸리는 시간
            if time <= b_move: 
                time = 1 # 이미 대기중인 상태이면 버튼을 누르기만 하면 된다.
            else: 
                time -= b_move-1 # 남은거리만큼 이동 + 버튼 누르기
            tot_time += time
            o_move += time # 블루가 누르는데 걸리는 시간만큼 오렌지는 자유롭게 이동가능
            b_btn = int(string[btn*2]) # 현재위치 갱신
            b_move = 0 # 초기화
        else: 
            time = abs(o_btn - int(string[btn*2])) # 이전 위치에서 버튼을 누르러 가는데 걸리는 시간
            if time <= o_move: 
                time = 1 # 이미 대기중인 상태이면 버튼을 누르기만 하면 된다.
            else: 
                time -= o_move-1 # 남은거리만큼 이동 + 버튼 누르기
            tot_time += time
            b_move += time # 오렌지가 누르는데 걸리는 시간만큼 블루는 자유롭게 이동가능
            o_btn = int(string[btn*2]) # 현재위치 갱신
            o_move = 0 # 초기화
    print(f'#{tc} {tot_time}')