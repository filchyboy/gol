class Cell:
    def __init__(self, awake=None, cell_x=None, cell_y=None):
        self.awake = awake
        self.cell_x = cell_x
        self.cell_y = cell_y

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def delete(self):
        self.value = None
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node
        self.tail = new_node

    def display(self):
        elements = []
        cur_node = self.head
        while self.head is not None:
            elements.append(self.head.value)
            while cur_node.next_node is not None:
                cur_node = cur_node.next_node
                elements.append(cur_node.value)
            return elements

    def length(self):
        cur_node = self.head
        total = 1
        while cur_node.next_node is not None:
            total += 1
            cur_node = cur_node.next_node
        return total

    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head
        while(current is not None):
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous