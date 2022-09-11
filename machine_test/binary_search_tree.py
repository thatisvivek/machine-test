"""Binary search tree"""


class BST:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add(self, item):
        if item < self.data:
            if self.left is None:
                self.left = BST(item)
            else:
                self.left.add(item)
        else:
            if self.right is None:
                self.right = BST(item)
            else:
                self.right.add(item)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print(self.data)

        if self.right is not None:
            self.right.print_in_order()
