class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 99999

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min