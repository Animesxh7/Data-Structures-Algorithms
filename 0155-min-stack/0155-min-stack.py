class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []
    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.minst or value <= self.minst[-1]:
            self.minst.append(value)
    def pop(self) -> None:
        x = self.st.pop()
        if x == self.minst[-1]:
            self.minst.pop()
    def top(self) -> int:
        return self.st[-1]
    def getMin(self) -> int:
        return self.minst[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()