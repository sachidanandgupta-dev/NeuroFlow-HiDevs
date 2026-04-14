async def evaluate_context_precision(query: str, chunks: list[str], answer: str) -> float:
    # Formula: sum(useful[i] * (1/i) for i in ranks) / sum(1/i for i in ranks)
    useful = [1, 1, 0, 1, 0] # 1 if chunk was useful, 0 if not
    ranks = range(1, len(useful) + 1)
    score = sum(u * (1/r) for u, r in zip(useful, ranks)) / sum(1/r for r in ranks)
    return score