"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            return None
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
            elif value == self.value:
                self.right = BSTNode(value)
        else:
            self.value = value

    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    def get_max(self):
        if self.right is None:
            return self.value
        max_val = self.right.get_max()
        return max_val

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    def in_order_print(self, node):
        if node is None:
            return None
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    def bft_print(self, node):
        queue = []
        if node:
            queue.append(node)
            print(node.value)
        current = node
        while current:
            if current.left:
                print(current.left.value)
                queue.append(current.left)
            if current.right:
                print(current.right.value)
                queue.append(current.right)
            queue.pop(0)
            if not queue:
                break
            current = queue[0]

    def dft_print(self, node):
        stack = [node]
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)

    # Stretch Goals -------------------------

    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
