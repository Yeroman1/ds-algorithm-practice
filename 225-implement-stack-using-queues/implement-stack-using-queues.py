class MyStack:

    def __init__(self):
        self.sq=deque()

    def push(self, x: int) -> None:
        self.sq.append(x)
        for i in range(len(self.sq) - 1):
            self.sq.append(self.sq.popleft())

    def pop(self) -> int:
        return self.sq.popleft()

    def top(self) -> int:
        return self.sq[0]

    def empty(self) -> bool:
        return len(self.sq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()