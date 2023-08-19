class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# linked list: 1 -> 2 -> 3 -> 4 -> 5
nodes = [ListNode(i) for i in range(1, 6)]
for i in range(4):
    nodes[i].next = nodes[i+1]
reversed_head = reverse_linked_list(nodes[0])