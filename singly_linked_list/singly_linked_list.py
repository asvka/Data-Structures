class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        output: ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.next} => '
            current_node = current_node.next
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def get_max(self):
        if not self.head:
            return None
        curr = self.head
        maximum = self.head.value

        while curr:
            if curr.value > maximum:
                maximum = curr.value
            curr = curr.next_node
        return maximum

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False


# linked_list = LinkedList()
#
# linked_list.add_to_head(0)
# linked_list.add_to_tail(2)
# print(f'Contains 0? {linked_list.contains(0)}')
# print(f'Contains 2? {linked_list.contains(2)}')
