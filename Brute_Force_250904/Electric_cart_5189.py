def DFS(cur, battery, visited, N): # DFS를 통해 모든 루트를 돈다
    if visited: # visited가 비어있으면 인덱스 에러가 발생하므로 visited가 있을 때만 검사
        if visited[-1] == 0 and len(visited) != N:  # 0으로 돌아왔는데 모든곳을 돌지 않았을 때
            return None                             # 무시
        elif visited[-1] == 0 and len(visited) == N:# 모든 곳을 돌아서 0으로 돌아온 경우
            battery_list.add(battery)               # 소모 배터리를 리스트에 저장
            return None
    for next_field in range(N): # 각 간선마다 DFS분기
        if adjacency_matrix[cur][next_field] == 0: continue # 0이면 무시(길이 없다는 뜻)
        if next_field not in visited: # 다음으로 가는 노드가 방문하지 않았으면 
            visit = visited.copy()    # 새 visited를 만들어서 방문 처리 후 DFS분기
            visit.append(next_field)  # 분기할 때 소모한 배터리를 더해서 넣어준다.
            new_batt = battery + adjacency_matrix[cur][next_field]
            DFS(next_field, new_batt, visit, N)


T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    adjacency_matrix = list(list(map(int, input().split())) for _ in range(N))
    battery_list = set()
    DFS(0, 0, [], N)
    print(f'#{tc} {min(battery_list)}')

"""
adjacency_matrix(인접행렬)은 노드에서 노드로 이동할 때의 가중치 또는 연결 여부를 표시하기 위한
그래프의 구성방법 중 하나이고 행은 출발지, 열은 도착지를 의미하고 [행][열]은 연결여부 또는 가중치를
의미한다. 
이 문제에서 는 인접행렬[2][1]의 값은 2번 노드에서 1번노드로 가는 간선의 가중치를 의미한다.
"""