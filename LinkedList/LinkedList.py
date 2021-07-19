class Node():
    def __init__(self, value, next_node=None):
        self.val = value
        self.next = next_node

# Insert new node to linked list
#
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        n = Node(val)
        n.next = self.head
        self.head = n

    def delete(self, val):
        dh = Node(-1)
        dh.next = self.head
        previous = dh
        current = self.head
        while current:
            if current.val == val:
                previous.next = current.next
                return dh.next
            previous = current 
            current = current.next
        return dh.next

    def toString(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
        print("---")

a = Node(3)

# 1 -> 2 -> 3
#
list = LinkedList()
list.head = a
list.toString()

# insert test
#
list.insert(2)
list.insert(1)
list.toString()



