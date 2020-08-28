class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.current = 0

    def append(self, item):
        # case 1: list is not full
        if len(self.list) < self.capacity:
            return self.list.append(item)
        # case 2: list is full
        else:
            if self.current == self.capacity:
                self.current = 0
            self.list[self.current] = item
            self.current = self.current + 1

    def get(self):
        if type(self.list) is not list:
            return []
        return self.list
