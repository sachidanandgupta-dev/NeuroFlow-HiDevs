from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse
import asyncio
import json

router = APIRouter()

@router.get("/query/{run_id}/stream")
async def stream_query(run_id: str):
    async def event_generator():
        # Step 1: Retrieval Start
        yield {"data": json.dumps({"type": "retrieval_start"})}
        await asyncio.sleep(0.5)
        
        # Step 2: Retrieval Complete
        yield {"data": json.dumps({"type": "retrieval_complete", "chunk_count": 5, "sources": ["doc1.pdf"]})}
        
        # Step 3: Stream Tokens (Mock for testing)
        tokens = ["Based", " on", " the", " context,", " the", " answer", " is..."]
        for token in tokens:
            yield {"data": json.dumps({"type": "token", "delta": token})}
            await asyncio.sleep(0.1)
        
        # Step 4: Done with Citations
        yield {"data": json.dumps({"type": "done", "run_id": run_id, "citations": []})}

    return EventSourceResponse(event_generator())