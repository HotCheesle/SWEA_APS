def s_push(char): 
    global top
    top += 1
    stack[top] = char

def s_peek(): 
    global top
    if top == -1: 
        return None
    return stack[top]

stack = [None for _ in range(100)]

for tc in range(1, 11): 
    N, string = input().split()
    idx, top = 0, -1
    for _ in range(len(string)): 
        if s_peek() == string[idx]: 
            top -= 1
        else: 
            s_push(string[idx])
        idx += 1
    print(f'#{tc} ', end='')
    for i in range(top+1): 
        print(stack[i], end='')
    print()