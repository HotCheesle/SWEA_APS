T = int(input())
for tc in range(1, 1+T): 
    N = int(input())
    job_list = []
    for _ in range(N): 
        js, je = map(int, input().split())
        job_list.append((js, je))
    job_list.sort(key=lambda job: job[1])
    idx, job_cnt, time = 0, 0, 0
    while idx != N: 
        if time > job_list[idx][0]: 
            idx += 1
            continue
        job_cnt += 1
        time = job_list[idx][1]
        idx += 1
    print(f'#{tc} {job_cnt}')