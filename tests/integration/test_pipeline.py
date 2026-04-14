import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_full_rag_pipeline():
    # 1. Upload a known document
    # Note: Ensure you have a PDF in tests/fixtures/test_doc.pdf
    doc_id = await ingest_test_document("tests/fixtures/test_doc.pdf")
    await wait_for_status(doc_id, "complete", timeout=60)

    # 2. Query for known content
    run_id = await submit_query("What is the main topic of the document?")

    # 3. Wait for generation
    response = await wait_for_generation(run_id, timeout=30)

    # 4. Assert retrieval happened
    assert response["chunks_used"] > 0

    # 5. Assert answer is non-empty
    assert len(response["generation"]) > 50

    # 6. Wait for evaluation
    eval_result = await wait_for_evaluation(run_id, timeout=120)
    assert eval_result["overall_score"] > 0.5