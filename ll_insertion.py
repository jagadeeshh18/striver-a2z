class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at head
    def insert_at_head(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    # Insert at tail
    def insert_at_tail(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    # Insert at position k (1-based indexing)
    def insert_at_position(self, data, k):
        newnode = Node(data)

        # Empty list
        if self.head is None:
            if k == 1:
                self.head = newnode
            else:
                print("Position out of bounds")
            return

        # Insert at head
        if k == 1:
            newnode.next = self.head
            self.head = newnode
            return

        cnt = 1
        temp = self.head
        while temp.next and cnt < k - 1:
            temp = temp.next
            cnt += 1

        if cnt == k - 1:
            newnode.next = temp.next
            temp.next = newnode
        else:
            print("Position out of bounds")

    # Insert before a given value
    def insert_before_value(self, data, val):
        newnode = Node(data)

        # Empty list
        if self.head is None:
            print("List is empty")
            return

        # Value is at head
        if self.head.data == val:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        while temp.next and temp.next.data != val:
            temp = temp.next

        if temp.next is None:
            print(f"Value {val} not found in the list")
            return

        newnode.next = temp.next
        temp.next = newnode

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")


ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_tail(40)
ll.insert_at_position(20, 2)
ll.insert_at_position(30, 3)
ll.insert_before_value(5, 10)
ll.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> 40 -> None
