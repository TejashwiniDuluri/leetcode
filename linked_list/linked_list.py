

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_begin(self, val):
        new_node = Node(val)
        if self.head:
            curr = self.head
            new_node.next = curr
            self.head = new_node
            self.size = self.size+1
        else:
            self.head = new_node
            self.size = self.size+1
            return

    def insert_at_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.size = self.size+1
            return
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.next = new_node
        self.size = self.size+1
        return

    def traverse(self):
        current = self.head

        while (current):
            print(current.val)
            current = current.next
        return

    def getsize(self):
        current = self.head

        size = 0
        while (current):
            size += 1
            current = current.next
        return size

    def remove_first_node(self):
        if not self.head:
            return
        else:
            self.head = self.head.next
            self.size = self.size-1

    def remove_last_node(self):
        if not self.head:
            return

        current = self.head
        # last but second node
        while (current.next.next):
            current = current.next

        current.next = None
        self.size = self.size-1
        return

    def insert_at_index(self, index, val):
        position = 0
        current = self.head

        if index < 0 or index > self.size + 2:
            return

        if index == 0:
            self.head = Node(val, current)
            self.size = self.size+1
            return

        else:
            print(index, self.size)
            prev = self.head
            while (position != index and position < self.size):

                prev = current
                current = current.next
                position = position+1

            if prev:
                prev.next = Node(val, current)
                self.size = self.size+1
            return

    def remove_at_index(self, index):
        position = 0
        current = self.head
        if index < 0 or index > self.size-1:
            return
        if index == 0:
            self.head = current.next
            self.size = self.size-1
            return
        else:
            prev = current

            while (position != index):

                prev = current
                current = current.next
                position = position+1
            if current:
                prev.next = current.next
                self.size = self.size-1
            return


obj = LinkedList()
obj.insert_at_end(0)
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.insert_at_end(4)
print(obj.traverse())
# print(obj.insert_at_index(5, 6))
print(obj.remove_at_index(0))
print(obj.traverse())

# print(obj.remove_last_node())


