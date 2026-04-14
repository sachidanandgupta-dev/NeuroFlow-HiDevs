# Quality Improvement Log

### Attempt 1: Parent-Child Chunking Strategy
- **What changed:** Switched from fixed 512-token chunks to Parent-Child chunking (small 128-token chunks for retrieval, 512-token parent chunks for context).
- **Why:** Smaller chunks allow for more precise vector matches, while the larger parent context helps the LLM generate better answers.
- **Metrics:** Hit Rate@10 improved from 0.72 to 0.81.
- **Decision:** Keep.

### Attempt 2: HNSW Parameter Tuning
- **What changed:** Increased `ef_search` parameter for the vector database from 100 to 300.
- **Why:** A higher `ef_search` value allows for more thorough exploration of the vector space during search.
- **Metrics:** Retrieval MRR@10 improved from 0.54 to 0.68.
- **Decision:** Keep.

### Attempt 3: One-Shot Prompt Refinement
- **What changed:** Added one-shot examples for complex query types to the system prompt and reduced overall prompt length.
- **Why:** Examples ground the LLM's response style, and shorter prompts improve instruction following and reduce latency.
- **Metrics:** Faithfulness improved from 0.71 to 0.82; Latency dropped below 4s.
- **Decision:** Keep.