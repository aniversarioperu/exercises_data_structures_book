class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[0]

    def size(self):
        return len(self.items)
