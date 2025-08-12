prime = [2, 3, 5, 7, 11]

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    count = [0, 0, 0, 0, 0]
    for i in range(5):
        while num % prime[i] == 0:
            num //= prime[i]
            count[i] += 1
            if num == 0: break
        if num == 0: break

    print(f'#{tc}', end=' ')
    for cnt in count:
        print(cnt, end=' ')
    print()