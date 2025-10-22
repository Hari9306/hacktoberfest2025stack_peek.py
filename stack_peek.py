class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[0]  # ❌ Should peek at top (last element)

s = Stack()
s.push(10)
s.push(20)
print(s.peek())  # Expected 20
