tree = ['' for _ in range(101)]

def inorder(index): 
    if index*2 <= N: 
        inorder(index*2)
    
    print(tree[index], end='')

    if index*2+1 <= N: 
        inorder(index*2+1)
    
for tc in range(1, 11): 
    N = int(input())
    for _ in range(N): 
        no, data, *son = input().split()
        tree[int(no)] = data
    print(f'#{tc} ', end='')
    inorder(1)
    print()