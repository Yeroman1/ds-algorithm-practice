class RecentCounter:
    def __init__(self):
        self.que=deque()
    def ping(self, t: int) -> int:
        queue=self.que
        queue.append(t)
        while queue[0]<t-3000:
            queue.popleft()
        return len(queue)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)