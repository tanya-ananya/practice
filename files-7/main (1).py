class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def insert_node(head, value):
    new_node = Node(value)
    current = head
    while current.next:
        current = current.next
    current.next = new_node

def delete_node(head, value):
    if head and head.value == value:
        return head.next
    previous = None
    current = head
    while current:
        if current.value == value:
            previous.next = current.next  
            return head 
        previous = current
        current = current.next
    return head
