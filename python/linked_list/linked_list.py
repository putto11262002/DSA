class Node: 
    def __init__(self, val: int, next: 'Node' = None) -> None:
        self.val = val
        self.next = next



def gen_linked_list_from_list(arr: 'list[int]'): 
    head = None
    runner = None
    for item in arr: 
        if head is None:
            runner = Node(item)
            head = runner
        else: 
            runner.next = Node(item)
            runner = runner.next
    return head


def to_string(head: 'Node'): 
    parts = []
    runner = head
    while runner is not None: 
      
        parts.append(f'{runner.val} -> ')
        runner = runner.next
    parts.append("None")
    return ''.join(parts)


