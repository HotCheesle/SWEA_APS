"""
50개의 TC에 대해 3초이므로 각 TC마다 약 180만번의 연산이 가능하다. 모든 지점에 대해서 각 K별로 해서
손해를 보지 않는 선에서 점점 크기를 늘려가면서 집의 최대 개수를 센다 400*400
"""
from collections import deque

def cover_gain(i, j, N, M): 
    queue = deque([(i, j)])
    visited = set()
    visited.add((i, j))
    deli, delj = [-1, 0, 1, 0], [0, 1, 0, -1]
    if city[i][j] == 1: 
        max_house = 1
        house = 1
    else: 
        max_house = 0
        house = 0
    for k in range(1, N*2): 
        added = len(queue)
        for _ in range(added): 
            cur = queue.popleft()
            for di, dj in zip(deli, delj): 
                newi, newj = cur[0]+di, cur[1]+dj
                if 0 <= newi < N and 0 <= newj < N and (newi, newj) not in visited: 
                    queue.append((newi, newj))
                    visited.add((newi, newj))
                    if city[newi][newj] == 1: 
                        house += 1
        gain = house * M - K[k]
        if gain > 0: 
            max_house = house
    return max_house



K = [1 for _ in range(40)] # 운영비용
for i in range(1, 40): 
    K[i] = K[i-1] + (i+1)*2 + (i-1)*2

T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    city = list(list(map(int, input().split())) for _ in range(N))
    max_cover = 1
    for i in range(N): 
        for j in range(N): 
            house = cover_gain(i, j, N, M)
            if house > max_cover: 
                max_cover = house
    print(f'#{tc} {max_cover}')