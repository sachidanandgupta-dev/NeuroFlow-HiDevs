# NeuroFlow System Architecture

## 1. Ingestion Subsystem
- **Goal**: Process PDF, DOCX, and Web URLs into vector embeddings.
- **Tech**: LangChain for extraction, Semantic Chunking, and pgvector for storage.

## 2. Retrieval Subsystem
- **Goal**: High-precision context fetching.
- **Flow**: Hybrid Search (Vector + BM25) -> RRF Fusion -> Cross-Encoder Reranking.

## 3. Generation Subsystem
- **Goal**: LLM responses with streaming.
- **Flow**: Model Routing (GPT-4o/Claude) -> Token Streaming -> logging to Postgres.

## 4. Evaluation Subsystem
- **Goal**: Quality assurance using "LLM-as-a-Judge".
- **Metrics**: Faithfulness, Relevance, and Precision stored in Postgres.

## 5. Fine-Tuning Subsystem
- **Goal**: Continuous improvement.
- **Flow**: High-score log extraction -> JSONL formatting -> LoRA training via MLflow.