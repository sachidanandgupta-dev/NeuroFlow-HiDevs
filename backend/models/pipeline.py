from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class IngestionConfig(BaseModel):
    chunking_strategy: str
    chunk_size_tokens: int
    chunk_overlap_tokens: int
    extractors_enabled: List[str]

class RetrievalConfig(BaseModel):
    dense_k: int
    sparse_k: int
    reranker: str
    top_k_after_rerank: int
    query_expansion: bool
    metadata_filters_enabled: bool

class GenerationConfig(BaseModel):
    model_routing: Dict[str, float] # e.g. {"task_type": "rag_generation", "max_cost_per_call": 0.05}
    max_context_tokens: int
    temperature: float
    system_prompt_variant: str

class EvaluationConfig(BaseModel):
    auto_evaluate: bool
    training_threshold: float

class PipelineConfig(BaseModel):
    name: str
    description: str
    version: int = 1
    ingestion: IngestionConfig
    retrieval: RetrievalConfig
    generation: GenerationConfig
    evaluation: EvaluationConfig