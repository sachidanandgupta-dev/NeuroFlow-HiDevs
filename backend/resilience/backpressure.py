def check_backpressure(queue_depth: int):
    if queue_depth > 100:
        return {"status": 503, "error": "ingestion_queue_full", "retry_after": 30}
    if queue_depth > 50:
        return {"status": 202, "warning": "high_queue_depth", "estimated_wait_minutes": queue_depth // 5}
    return {"status": 200, "message": "ok"}