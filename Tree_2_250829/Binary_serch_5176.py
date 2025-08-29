def rev_inorder(idx): 
    global num
    if idx*2 < N+1: 
        rev_inorder(idx*2)
    binary_tree[idx] = num
    num += 1
    if idx*2+1 < N+1: 
        rev_inorder(idx*2+1)

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    binary_tree = [0 for _ in range(N+1)]
    num = 1
    rev_inorder(1)
    print(f'#{tc} {binary_tree[1]} {binary_tree[N//2]}')