class RecentCounter:

    def __init__(self):
        self.queue = []
        self.length = 0

    def ping(self, t: int) -> int:
        start = t - 3000
        while self.queue and self.queue[0] < start:
            self.queue.pop(0)
            self.length -= 1

        self.queue.append(t)
        self.length += 1

        return self.length


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
["RecentCounter", "ping", "ping", "ping", "ping"]

print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
print(obj.ping(3003))
