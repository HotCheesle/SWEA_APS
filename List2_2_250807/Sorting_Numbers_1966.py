def selection_sort(arr, n): 
    for i in range(n-1): 
        min_idx = i
        for idx in range(i+1, n): 
            if arr[min_idx] > arr[idx]: 
                min_idx = idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


T = int(input())
for tc in range(1, T+1): 
    n = int(input())
    num_list = list(map(int, input().split()))

    num_list = selection_sort(num_list, n)
    print(f'#{tc} {" ".join(map(str, num_list))}')