{
  "status": "degraded",
  "checks": {
    "postgres": {"status": "ok", "latency_ms": 3},
    "redis": {"status": "ok", "latency_ms": 1},
    "circuit_breakers": {
      "openai": {"state": "closed", "failure_count": 0},
      "anthropic": {"state": "open", "opened_at": "2024-01-15T10:23:00Z"}
    }
  }
}