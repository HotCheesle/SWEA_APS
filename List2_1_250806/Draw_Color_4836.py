T = int(input())
for tc in range(1, T+1):
    paper = list(list(0 for _ in range(10)) for _ in range(10))
    N = int(input())
    for _ in range(N):
        square = list(map(int, input().split()))
        for row in range(square[0], square[2]+1):
            for col in range(square[1], square[3]+1):
                paper[row][col] += square[4]

    purple = 0
    for row in range(10):
        for col in range(10):
            if paper[row][col] == 3:
                purple += 1
    print(f'#{tc} {purple}')