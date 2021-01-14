"""Stack implementation using array"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not len(self.stack):
            print("No element in the stack.")
            return
        self.stack.pop()

    def is_empty(self):
        if not len(self.stack):
            print("Stack is empty")

    def print_stack(self):
        self.stack.reverse()
        print(self.stack)


stack = Stack()
stack.is_empty()
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
stack.pop()
stack.print_stack()
