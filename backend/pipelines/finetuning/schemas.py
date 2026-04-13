from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class TrainingPair(BaseModel):
    id: UUID
    query: str
    context: str
    answer: str
    quality_score: float
    faithfulness_score: Optional[float]
    created_at: str
    domain: str
