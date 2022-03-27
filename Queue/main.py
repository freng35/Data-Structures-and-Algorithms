class Queue:
    def __init__(self, _capacity):
        self.size = 0
        self.front = self.size
        self.back = _capacity - 1
        self.q = [None] * _capacity
        self.capacity = _capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, _value):
        if self.is_full():
            return

        self.back = (self.back + 1) % self.capacity
        self.q[self.back] = _value
        self.size += 1

    def pop(self):
        if self.is_empty():
            return

        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def top(self):
        if self.is_empty():
            return None
        return self.q[self.front]

    def last(self):
        if self.is_empty():
            return None
        return self.q[self.back]


def main():
    queue = Queue(5)

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue.top())

    queue.pop()

    print(queue.top())


if __name__ == '__main__':
    main()
