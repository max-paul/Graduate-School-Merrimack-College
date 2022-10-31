
class Stack:
    def __init__(self):
        self.self = self
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None

    def size(self):
        return len(self.elements)

    def empty(self):
        return True if self.size() == 0 else False

    # get elem at top of stack
    def peek(self):
        return self.elements[-1]
