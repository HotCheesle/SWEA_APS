import math

def calculate(root): 
    if tree[root][0] == '+': 
        return calculate(tree[root][1][0]) + calculate(tree[root][1][1])
    elif tree[root][0] == '-': 
        return calculate(tree[root][1][0]) - calculate(tree[root][1][1])
    elif tree[root][0] == '*': 
        return calculate(tree[root][1][0]) * calculate(tree[root][1][1])
    elif tree[root][0] == '/': 
        return calculate(tree[root][1][0]) // calculate(tree[root][1][1])
    else: 
        return int(tree[root][0])

for tc in range(1, 11): 
    tree = {}
    N = int(input())
    for _ in range(N): 
        inpt = list(input().split())
        tree[inpt[0]] = [inpt[1], inpt[2:]]
    print(f'#{tc} {math.floor(calculate("1"))}')