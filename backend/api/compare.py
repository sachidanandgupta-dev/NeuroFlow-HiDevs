import asyncio
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CompareRequest(BaseModel):
    query: str
    pipeline_a_id: str
    pipeline_b_id: str

async def mock_run_pipeline(pipeline_id: str, query: str):
    # This simulates running a specific RAG configuration
    await asyncio.sleep(0.5) # Simulate latency
    return {
        "run_id": f"run-{pipeline_id}",
        "generation": "Sample response from the LLM...",
        "retrieval_latency_ms": 234,
        "total_latency_ms": 1450,
        "chunks_used": 6,
        "eval_score": 0.87
    }

@router.post("/pipelines/compare")
async def compare_pipelines(request: CompareRequest):
    # Run both pipelines simultaneously using asyncio.gather
    res_a, res_b = await asyncio.gather(
        mock_run_pipeline(request.pipeline_a_id, request.query),
        mock_run_pipeline(request.pipeline_b_id, request.query)
    )
    
    return {
        "query": request.query,
        "pipeline_a": res_a,
        "pipeline_b": res_b
    }