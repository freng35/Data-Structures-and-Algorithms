class Node:
    def __init__(self, _value):
        self.value = _value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node: Node):
        self.head = node

    def append(self, root: Node, _value):
        if _value > root.value:
            if root.right is None:
                root.right = Node(_value)
            else:
                self.append(root.right, _value)
        elif _value < root.value:
            if root.left is None:
                root.left = Node(_value)
            else:
                self.append(root.left, _value)

    def min_value_node(self, node: Node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def del_node(self, root: Node, _value):
        if root is None:
            return root

        if _value < root.value:
            root.left = self.del_node(root.left, _value)
        elif _value > root.value:
            root.right = self.del_node(root.right, _value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.del_node(root.right, temp.value)

        return root

    def print_inorder(self, root: Node):
        if root:
            self.print_inorder(root.left)
            print(root.value)
            self.print_inorder(root.right)


def main():
    node = Node(2)
    tree = Tree(node)
    tree.append(node, 5)
    tree.append(node, 4)
    tree.append(node, 1)
    tree.append(node, 0)
    tree.append(node, 3)
    tree.append(node, 6)
    tree.append(node, -2)

    tree.print_inorder(node)
    print()
    node = tree.del_node(node, 0)
    tree.print_inorder(node)


if __name__ == '__main__':
    main()
