class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack = [0]
        else:
            if val > self.stack[self.minstack[-1]]:
                self.minstack.append(self.minstack[-1])
            else:
                self.minstack.append(len(self.minstack))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minstack[-1]]
