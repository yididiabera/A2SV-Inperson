class MyStack:

    def __init__(self):
        self.q = deque()        

    def push(self, x: int) -> None:
        self.q.append(x)
        
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
    # def __init__(self):
    #     self.q1 = deque()
    #     self.temp = deque()

    # def push(self, x: int) -> None:
    #     self.temp.append(x)

    #     while self.q1:
    #         self.temp.append(self.q1.popleft())
    #     self.q1, self.temp = self.temp, self.q1

    # def pop(self) -> int:
    #     return self.q1.popleft()

    # def top(self) -> int:
    #     return self.q1[0]

    # def empty(self) -> bool:
    #     return not self.q1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()