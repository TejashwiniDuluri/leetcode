class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        position = 0
        if index < 0 or index > self.size-1:
            return -1

        curr_node = self.head
        while index != position:
            curr_node = curr_node.next
            position = position+1
        return curr_node.val

    def addAtHead(self, val: int) -> None:
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

    def addAtTail(self, val: int) -> None:
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

    def addAtIndex(self, index: int, val: int) -> None:
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

    def deleteAtIndex(self, index: int) -> None:
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

    def traverse(self):
        current = self.head

        while (current):
            print(current.val)
            current = current.next
        return


# my_linked_list = MyLinkedList()
# print(my_linked_list.addAtHead(1))
# print(my_linked_list.addAtTail(3))
# print(my_linked_list.addAtIndex(1, 2))
# print("=====", "head")
# print(my_linked_list.traverse())
# print("=====")
# print(my_linked_list.get(1))              # return 2
# print("=====")
# print(my_linked_list.deleteAtIndex(1))    # now the linked list is 1->3
# print(my_linked_list.get(1))              # return 2
# print(my_linked_list.get(3))              # return 2
# print(my_linked_list.deleteAtIndex(3))    # now the linked list is 1->3
# print(my_linked_list.deleteAtIndex(0))    # now the linked list is 1->3
# print(my_linked_list.get(0))              # return 2
# print(my_linked_list.deleteAtIndex(0))    # now the linked list is 1->3
# print(my_linked_list.get(0))              # return 2

# print("=====", "delete======================")
# print(my_linked_list.traverse())
# print(my_linked_list.get(1))              # return 3
# print("=====")


##################

# my_linked_list = MyLinkedList()
# print(my_linked_list.addAtHead(7))
# print(my_linked_list.addAtHead(2))
# print(my_linked_list.addAtHead(1))

# print(my_linked_list.size, "*************")

# print(my_linked_list.addAtIndex(3, 0))
# print(my_linked_list.traverse())

# print(my_linked_list.size, "*************")

# print("=====", "head")
# print(my_linked_list.traverse())
# print("=====")
# print("=====")
# print(my_linked_list.deleteAtIndex(2))    # now the linked list is 1->3
# print(my_linked_list.addAtHead(6))
# print(my_linked_list.addAtTail(4))
# print(my_linked_list.get(4))              # return 3
# print(my_linked_list.addAtHead(4))
# print(my_linked_list.addAtIndex(5, 0))
# print(my_linked_list.addAtHead(6))

###########################


my_linked_list = MyLinkedList()
print(my_linked_list.addAtHead(1))
print(my_linked_list.addAtTail(3))
print(my_linked_list.size, "*************")

print(my_linked_list.addAtIndex(3, 2))
print(my_linked_list.traverse())
