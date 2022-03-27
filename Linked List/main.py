class Node:
    def __init__(self, _value):
        self.value = _value
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def append_node(self, node: Node):
        if not self.head:
            self.head = node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next

        tmp.next = node

    def delete_node(self, _value):
        if not self.head:
            return
        tmp = self.head

        if tmp.value == _value:
            self.head = tmp.next
            return

        prev = tmp
        tmp = tmp.next
        flag = False

        while tmp and not flag:
            if tmp.value == _value:
                prev.next = tmp.next
                flag = True
            prev = tmp
            tmp = tmp.next

    def show(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next
        print()


def main():
    linked_list = List()

    linked_list.append_node(Node(1))
    linked_list.append_node(Node(2))
    linked_list.append_node(Node(2))
    linked_list.append_node(Node(3))
    linked_list.append_node(Node(2))

    linked_list.show()

    linked_list.delete_node(2)

    linked_list.show()


if __name__ == '__main__':
    main()
