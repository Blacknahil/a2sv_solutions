class MyStack:

    def __init__(self):
        self.stack=deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        return self.stack.popleft()
        

    def top(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if self.stack:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()