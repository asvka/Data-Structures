"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        curr_next = self.next
        node = ListNode(value, self, curr_next)
        self.next = node
        if curr_next:
            curr_next.prev = self.next
        return node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        curr_prev = self.prev
        node = ListNode(value, curr_prev, self)
        self.prev = node
        if curr_prev:
            curr_prev.next = self.prev
        return node

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head:
            self.head = self.head.insert_before(value)
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head:
            return None
        value = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.delete(self.head)
        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.tail:
            return None
        value = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.delete(self.tail)
        self.length -= 1
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # the list is empty -> do nothing
        # the list is only one node

        if not self.head:
            return None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        if node == self.head:
            self.head = node.next
            node.delete()
        if node == self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        curr = self.head
        maximum = self.head.value

        while curr:
            if curr.value > maximum:
                maximum = curr.value
            curr = curr.next
        return maximum

