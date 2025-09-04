"""
이번 문제는 최대 10번 까지 스왑이 가능한데 순열 알고리즘은 O(n!)이라는 극악무도한
시간복잡도를 요구한다. 따라서 가지치기를 엄청나게 해줘야 한다!(10번 다 돌리면 15^10 = 5700억...)
전체적인 흐름은 다음과 같다. 

1. swap하는 index묶음을 모두 구한다. 3자리라면 (0, 1), (0, 2), (1, 2) | (0, 1) 이런거는 제외
    했었어야 되는데 으악
2. 이러한 index묶음의 인덱스를 중복순열로 구한다. ex) [0, 1, 1] -> 0, 1스왑, 0, 2스왑, 0, 2 스왑
3. 위해서 구한 순열로 순서대로 스왑한다.(이렇게 하기 위해서는 input을 한자씩 분리되어있는 리스트로 변환)
4. 이러한 스왑 결과물을 숫자로 만들어서 최대값과 비교한다.

이제 극한의 가지치기 작업이 들어가야 한다. 우선 두 숫자를 스왑하는데 가장 크게 만드려면 Selection Sort를
생각하면 편하다. 가장 큰 숫자를 가장 앞쪽과 스왑하는 것이다. 이렇게하면 자릿수가 가장 큰 6자리라도 
4번의 스왑을 거치면 가장 크거나 두번째로 크게 된다. (4번 스왑은 50,625번 밖에 안걸린다)
ex) 1에서 6이 있는 숫자라면 654321 또는 654312 일 수 밖에 없다. 

따라서 4회 이후의 스왑 작업은 둘 중 하나이다. 
    - 가장 낮은 자리 수 두개를 바꾸거나 
    - 같은 숫자가 있다면 그것을 바꾸거나 (이러면 숫자가 변하지 않는다. 항상 가장 큰숫자를 만들 수 있다)

이러한 가지치기를 위해서 4 이상의 스왑 작업은 모두 4로 만든 뒤 홀수번 남는다면 한번 스왑이 일어난다.
이때 숫자중 같은 숫자가 존재한다면 그것을 바꾸면 되므로 항상 가장 큰 값을 만들 수 있다.

뭔 조합이여 그냥 DFS씁시다
"""
def get_order(order, cnt, swap_cnt, swap_max_idx, order_list): # 스왑할 인덱스 묶음의 인덱스 순열 생성
    od = order.copy()                   # 새 order리스트 생성
    if cnt == swap_cnt: 
        order_list.append(od)
        return None
    else: 
        for idx in range(swap_max_idx): # n번째 자리에 0부터 끝까지 하나씩 넣는다.
            od[cnt] = idx
            get_order(od, cnt+1, swap_cnt, swap_max_idx, order_list)

def swap(number, order_list): # 리스트 순서대로 스왑 해주는 함수
    num = number.copy()
    for idx in order_list: 
        swap = swap_list[idx]
        num[swap[0]], num[swap[1]] = num[swap[1]], num[swap[0]]
    num_str = ''.join(num)
    return int(num_str) # 결과를 int로 반환

T = int(input())
for tc in range(1, T+1): 
    number, max_swap_cnt = input().split()
    max_swap_cnt = int(max_swap_cnt) # 문자열로 받은걸 int로 변환
    number = list(number)
    if len(number) != len(set(number)): # 같은 숫자가 있으면 ignore Flag True로 바꾸기
        ignore_final_swap = True
    else: 
        ignore_final_swap = False
    best = sorted(number.copy(), reverse=True) # 가장 큰 숫자
    length = len(number)
    if max_swap_cnt > 4: # 만약 스왑 횟수가 4보다 더 크면 4로 변경하고 홀짝에 따라 마지막 스왑을
        swap_cnt = 4     # 할지 말지 결정
        final_swap = (max_swap_cnt - 4) % 2
    else: 
        swap_cnt = max_swap_cnt
        final_swap = 0
    swap_list = [[x, y] for x in range(length) for y in range(length) if x != y] # 스왑 인덱스 묶음 생성
    order_list = [] # 여기에 순열을 담을 예정
    get_order([0 for _ in range(int(swap_cnt))], 0, int(swap_cnt), len(swap_list)-1, order_list)
    max_reward = 0 # 최대값 찾기위해 초기값 0으로 설정
    for order in order_list:         # 각 순열마다 순회하면서
        reward = swap(number, order) # 스왑한 결과를 받음
        if max_reward < reward:      # 최대값 갱신
            max_reward = reward
    if final_swap and not ignore_final_swap: # 마지막 스왑이 필요한 경우
        number = list(str(max_reward))       # 다시 리스트로 풀었다가 다시 묶음
        number[-1], number[-2] = number[-2], number[-1]
        max_reward = int(''.join(number))
    elif final_swap and ignore_final_swap: # 필요 없는 경우
        max_reward = int(''.join(best))    # 항상 최대 결과가 나옴
    print(f'#{tc} {max_reward}')