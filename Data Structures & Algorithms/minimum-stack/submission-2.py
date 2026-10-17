class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_index:
            min_index = self.min_index[-1]
            if val < self.stack[min_index]:
                self.min_index.append(len(self.stack) - 1)
            else:
                self.min_index.append(min_index)
        else:
            self.min_index.append(0)


    def pop(self) -> None:
        self.stack.pop()
        self.min_index.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_index:
            min_index = self.min_index[-1]
            return self.stack[min_index]
