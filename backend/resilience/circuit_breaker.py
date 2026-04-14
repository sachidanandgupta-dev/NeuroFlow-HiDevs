import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, name: str, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        # Note: In production, these should be stored in Redis
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.last_failure_time = 0

    def call(self):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception(f"Circuit {self.name} is OPEN")
        return True

    def record_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            self.last_failure_time = time.time()

    def record_success(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED