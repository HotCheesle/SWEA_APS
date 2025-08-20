class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

def enqueue(head, tail, data): 
    new_node = Node(data)
    if head is None or tail is None: 
        head = new_node
        tail = new_node
        return head, tail
    else: 
        tail.next = new_node
        new_node.pre = tail
        tail = new_node
        return head, tail

def dequeue(head, tail): 
    if head is None or tail is None: 
        return None
    else: 
        data = head.data
        head = head.next
        head.pre = None
        return head, tail, data

#######################################

def cycle(head, tail):
    sub = 0
    while tail.data > 0: 
        temp = head
        head = temp.next
        head.pre = None
        temp.next = None
        temp.data -= (sub%5)+1
        sub += 1
        tail.next = temp
        temp.pre = tail
        tail = temp
    tail.data = 0
    return head, tail

for tc in range(1, 11): 
    _ = input()
    num_list = list(map(int, input().split()))
    head, tail = None, None
    for num in num_list: 
        head, tail = enqueue(head, tail, num)
    head, tail = cycle(head, tail)
    print(f'#{tc}', end=' ')
    cur = head
    print(cur.data, end=' ')
    while cur.next is not None: 
        cur = cur.next
        print(cur.data, end=' ')
    print()