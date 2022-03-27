class Node:
    def __init__(self, _value):
        self.value = _value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node: Node):
        self.head = node

    def print_inorder(self, root: Node):
        if root:
            self.print_inorder(root.left)
            print(root.value)
            self.print_inorder(root.right)

    def print_postorder(self, root: Node):
        if root:
            self.print_postorder(root.left)
            self.print_postorder(root.right)
            print(root.value)

    def print_preorder(self, root: Node):
        if root:
            print(root.value)
            self.print_postorder(root.left)
            self.print_postorder(root.right)


def main():
    node = Node(2)                # 2
    node.left = Node(1)         # 1   5
    node.left.right = Node(3)  # - 3 - 6
    node.right = Node(5)
    node.right.right = Node(6)
    tree = Tree(node)
    tree.print_inorder(node)
    print()
    tree.print_postorder(node)
    print()
    tree.print_preorder(node)


if __name__ == '__main__':
    main()
