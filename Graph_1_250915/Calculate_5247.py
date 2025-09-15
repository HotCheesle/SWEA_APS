from collections import deque

def BFS(N, M): 
    queue = deque([(N, 0)])
    visited = set()
    while queue: 
        now = queue.popleft()
        if now[0] == M: 
            return now[1]
        if now[0] in visited: continue
        if now[0] < M: 
            queue.append((now[0]*2, now[1]+1))
            queue.append((now[0]+1, now[1]+1))
        queue.append((now[0]-1, now[1]+1))
        queue.append((now[0]-10, now[1]+1))
        visited.add(now[0])

T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    if M < N: 
        diff = N - M
        cnt = diff//10 + diff%10
        print(f'#{tc} {cnt}')
    else: 
        min_cnt = BFS(N, M)
        print(f'#{tc} {min_cnt}')