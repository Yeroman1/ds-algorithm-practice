class RecentCounter:
    def __init__(self):
        self.r=[]
        self.c=0
    def ping(self, t: int) -> int:
        self.r.append(t)
        while self.r[self.c] < t-3000:
            self.c+=1
        return len(self.r)-self.c
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)