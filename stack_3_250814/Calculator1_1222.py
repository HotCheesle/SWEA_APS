num_stack = []
plus_stack = []

for tc in range(1, 11): 
    num_stack.clear() 
    plus_stack.clear()
    N = int(input())
    string = input()
    for tok in string: 
        if tok == '+': 
            plus_stack.append(tok)
        else: 
            num_stack.append(int(tok))
    for _ in range(len(plus_stack)): 
        x1 = num_stack.pop()
        x2 = num_stack.pop()
        result = x2 + x1
        num_stack.append(result)
    print(f'#{tc} {num_stack.pop()}')