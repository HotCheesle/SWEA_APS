"""
1 <= N <= 400 이고 시간제한 2초이므로 최대 6천만번의 연산 가능 TC가 10개이므로 
TC하나 당 600만번 연산가능 n^3까지도 커버가 가능하다
>> 200 배열에 각 학생별로 동선을 더하면 가능 200*400 8만번만 하면 됨
"""

T = int(input())
for tc in range(1, T+1): 
    hallway = [0 for _ in range(200)]
    N = int(input())
    for _ in range(N): 
        st, ed = map(int, input().split())
        s = min((st-1)//2, (ed-1)//2)
        e = max((st-1)//2, (ed-1)//2)
        for i in range(s, e + 1): 
            hallway[i] += 1
    print(f'#{tc} {max(hallway)}')