async def evaluate_faithfulness(query: str, answer: str, context: str) -> float:
    # 1. Extract factual claims from answer (LLM Prompt)
    # 2. For each claim, check support in context (LLM Prompt)
    # Mocking logic for structure:
    total_claims = 5
    supported_claims = 4.5 # Example including a "partial" count (0.5)
    
    if not context and answer: return 0.0
    return supported_claims / total_claims