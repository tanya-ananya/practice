class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def iterate(head):
    lst = []
    current = head
    while current.next:
        lst.append(current.value)
        current = current.next
    return lst

def delete(head, target_node):
    if head is None:
        return None
    previous = None
    current = head
    while current.value < target_node.value:
        previous = current
        current = current.next
    if current.value == target_node.value:
        previous.next = current.next
        current = previous.next
    print(f'Previous {previous.value}, current = {current.value}')

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
print(iterate(node1))
delete(node1, node3)