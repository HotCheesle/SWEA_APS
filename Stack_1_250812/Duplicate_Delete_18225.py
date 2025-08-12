def s_push(char): 
    global top
    top += 1
    stack[top] = char

def s_peek(): 
    global top
    if top == -1: 
        return None
    return stack[top]

stack = [None for _ in range(1000)]

T = int(input())
for tc in range(1, T+1): 
    top = -1
    string = input()
    for i in range(len(string)): 
        if string[i] != s_peek(): 
            s_push(string[i])
        else: 
            top -= 1
    
    print(f'#{tc} {top+1}')