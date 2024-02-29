class MinStack:

    def __init__(self):
        self.stack=[(float("inf"),float("inf"))]
        

    def push(self, val: int) -> None:
        _min=min(self.stack[-1][1],val)
        self.stack.append((val,_min))
        
    def pop(self) -> None:
        popped=self.stack.pop()
        return popped[0]

    def top(self) -> int:
        top=self.stack[-1]
        return top[0]
        

    def getMin(self) -> int:
        top=self.stack[-1]
        return top[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()