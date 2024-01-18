class MinStack:

    def __init__(self):
        self.MinStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack or val <= self.MinStack[-1]:
            self.MinStack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.MinStack[-1]:
                self.MinStack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.MinStack:
            return self.MinStack[-1]
