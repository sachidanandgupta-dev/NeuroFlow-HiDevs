import time

class TokenBucket:
    def __init__(self, capacity: int, fill_rate: float):
        self.capacity = capacity
        self.fill_rate = fill_rate # tokens per second
        self.tokens = capacity
        self.last_fill = time.time()

    def consume(self, tokens: int = 1):
        now = time.time()
        # Refill tokens based on time passed
        self.tokens = min(self.capacity, self.tokens + (now - self.last_fill) * self.fill_rate)
        self.last_fill = now
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False