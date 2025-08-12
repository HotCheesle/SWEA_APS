def spacial_sort(arr, n): 
    for i in range(n-1): 
        if i % 2 == 0: # big
            max_idx = i
            for idx in range(i, n): 
                if arr[max_idx] < arr[idx]: 
                    max_idx = idx
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else: # small
            min_idx = i
            for idx in range(i, n): 
                if arr[min_idx] > arr[idx]: 
                    min_idx = idx
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

T = int(input())
for tc in range(1, T+1): 
    n = int(input())
    num_list = list(map(int, input().split()))
    num_list = spacial_sort(num_list, n)

    print(f'#{tc} {" ".join(map(str, num_list[:10]))}')
