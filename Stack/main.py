class Stack:
    def __init__(self):
        self.array = []
        self.size = 0

    def push(self, _value):
        self.array = [_value] + self.array
        self.size += 1

    def isempty(self):
        return self.size == 0

    def pop(self):
        if self.isempty():
            return

        self.array = self.array[1:]
        self.size -= 1

    def show(self):
        for i in range(self.size):
            print(self.array[i])

        print()


def main():
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    s.show()

    s.pop()

    s.show()


if __name__ == '__main__':
    main()
