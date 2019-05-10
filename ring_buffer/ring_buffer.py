class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current != self.capacity:  # 1
            self.storage[self.current] = item  # 1
            self.current += 1  # 1
        else:  # 1
            self.current = 0  # 1
            self.append(item)  # 1

    def get(self):
        items = []
        for item in self.storage:
            if item != None:
                items.append(item)
            else:
                break
        return items


# rb = RingBuffer(5)

# rb.append('a')
# rb.append('b')
# rb.append('c')
# rb.append('d')
# rb.append('e')
# rb.append('f')

# print(rb.get())
