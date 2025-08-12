"""
import sys
sys.stdin = open(input.txt)
"""

for tc in range(1, 11):
    t = int(input()) # 사용하지 않음
    bingo = list(list(map(int, input().split())) for _ in range(100))

    sum_list = []

    for row in range(100):
        tot, tot2 = 0, 0
        for col in range(100):
            tot += bingo[row][col]
            tot2 += bingo[col][row]
        sum_list.append(tot)
        sum_list.append(tot2)
    tot, tot2 = 0, 0
    for rc in range(100):
        tot += bingo[rc][rc]
        tot2 += bingo[99-rc][rc]
    sum_list.append(tot)
    sum_list.append(tot2)

    max_sum = sum_list[0]
    for s in sum_list:
        if max_sum < s:
            max_sum = s

    print(f'#{tc} {max_sum}')
